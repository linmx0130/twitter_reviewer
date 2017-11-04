import urllib
import base64
import requests
import json

class TwitterAPI:
    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = None
    
    def encoded_confidential(self):
        key_code = self.consumer_key
        secret_code = self.consumer_secret
        code = base64.encodestring((key_code+':'+secret_code).encode())
        return code.decode().strip()

    def fetch_bearer_key(self):
        url = 'https://api.twitter.com/oauth2/token'
        headers = {
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
        body = 'grant_type=client_credentials'
        res = requests.post(url, headers=headers, data=body, auth=requests.auth.HTTPBasicAuth(self.consumer_key, self.consumer_secret))
        if res.ok:
            res_json = json.loads(res.content.decode())
            self.access_token = res_json['access_token']
            return self.access_token
        else:
            raise IOError(res.content.decode())

    def get_timelines_by_screen_name(self, screen_name):
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
        params = {'screen_name':screen_name, 'count':7}
        headers = {'Authorization': 'Bearer {}'.format(self.access_token)}
        res = requests.get(url, params=params, headers=headers)
        return res.json()
    
    def get_user_name_and_image(self, screen_name):
        url = 'https://api.twitter.com/1.1/users/show.json'
        params = {'screen_name': screen_name}
        headers = {'Authorization': 'Bearer {}'.format(self.access_token)}
        res = requests.get(url, params=params, headers=headers)
        if res.ok:
            res_json = res.json()
            name = res_json['name']
            image = res_json['profile_image_url']
            return name, image
        else:
            raise IOError()
