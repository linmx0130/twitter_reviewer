import requests
import json
import urllib 
class WastonEmotion:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def getEmotion(self, s):
        url = 'https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?'
        params_str = urllib.parse.urlencode({'version':'2017-02-27', 'text':s, 'features':'emotion'}, quote_via=urllib.parse.quote)
        url = url + params_str
        ret = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.username, self.password))
        result = json.loads(ret.content.decode())
        return result