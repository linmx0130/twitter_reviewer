from flask import Flask
from flask import url_for
from waston_api import WastonEmotion
from twitter_api import TwitterAPI
from datetime import datetime
from config import cfg

app = Flask(__name__, static_url_path='/static')

def get_max_score_key(emotion_scores):
    ret = 'None'
    s = 0
    for k in emotion_scores:
        if emotion_scores[k] > s:
            s = emotion_scores[k]
            ret = k
    return ret


@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/eval_emotion/<twitter_name>")
def eval_emotion(twitter_name):
    print("Start evaluating")
    waston_emotion = WastonEmotion(cfg.waston_name, cfg.waston_password)
    twitter_api = TwitterAPI(cfg.twitter_key, cfg.twitter_secret)
    twitter_api.fetch_bearer_key()

    data = twitter_api.get_timelines_by_screen_name(twitter_name)
    print("Data fetched")
    
    ret = "<!DOCTYPE html><html><head><title>Show Items</title><script type='text/javascript' src='../static/jquery.js'></script> \
         <script type='text/javascript' src='../static/main.js'></script><script>"
     
    username, profile_image_url = twitter_api.get_user_name_and_image(twitter_name)
    ret += 'profile_image_url="{}";'.format(profile_image_url)
    ret += 'username="{}";'.format(username)
    ret += 'background_file_name="../static/background02.png";'
    ret += 'fear="#D0C9C1";'
    ret += 'sadness="#C4CCC7";'
    ret += 'joy="#F4DFC1";'
    ret += 'angry="#D5BBAA";'
    ret += 'disgust="#988A81";\n'
    ret += 'color_list=['

    color_list = []
    emotion_list = []
    for item in data:
        res = waston_emotion.getEmotion(item['text'])
        if 'emotion' in res:
            emotion_list.append(get_max_score_key(res['emotion']['document']['emotion']))
            print(item['text'])

    emotion_count = len(emotion_list)
    for idx, item in enumerate(emotion_list):
        ret += "[{},{}],".format(idx/(emotion_count - 1), item)
    ret+="];\n"
    ret+= "</script></head><body><canvas id='canvas1' height='640', width='932'></canvas></body></html>"
    return ret
