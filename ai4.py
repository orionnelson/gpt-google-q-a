
import requests
import json
remove_input = 'true'
response_length = 200
temp = 0.8
top_p = 0.9
top_k = 40

content_length = 153
bearer_token =  '842a11464f81fc8be43ac76fb36426d2'
url_options = 'https://api.textsynth.com/v1/engines/gptj_6B/completions'
url = 'https://api.textsynth.com/v1/engines/gptj_6B/completions'
headers_options={
                'Accept-Encoding': "gzip, deflate, br",
                'Accept-Language':'en-CA,en-US;q=0.7,en;q=0.3',
                'Accept-Control-Request-Headers':'authorization,content-type',
                'Accept-Control-Request-Method':'POST',
                'Cache-Control':'no-cache',
                'Connection':'keep-alive',
                'Host': "api.textsynth.com",
                'Origin': "https://textsynth.com",
                'Content-Type' : "application/json",
                'Pragma':'no-cache',
                'Accept': "application/json",
                'Referer': "https://textsynth.com/",
                'Sec-Fetch-Dest' : "empty",
                'Sec-Fetch-Mode' : 'cors',
                'Sec-Fetch-Site' : 'same-site',
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
    
    }

headers = {
    'Accept-Encoding': "gzip, deflate, br",
    'Authorization': 'Bearer %s' % bearer_token,
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Length': '%s' % content_length,
    'Content-Type' : 'application/json',
    'Host': 'api.textsynth.com',
    'Origin': "https://textsynth.com",
    'Pragma':'no-cache',
    'Referer': "https://textsynth.com/",
    'Sec-Fetch-Dest' : "empty",
    'Sec-Fetch-Mode' : 'cors',
    'Sec-Fetch-Site' : 'same-site',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
}



def request(context):
    
    response = requests.options(url_options,allow_redirects=False, headers=headers_options)
    result = requests.post(url,allow_redirects=False, json={
                    "prompt": context,
                    "remove_input": remove_input,
                    "max_tokens": response_length,
                    "temprature": temp,
                    "top_p": top_p,
                    'top_k' : top_k,
            },headers=headers)
    if result.status_code == 200:
        out = json.loads(result.text)
        return out['text']
    else:
        print(result.text)
        return 'error'




"""
context = pyperclip.paste()
print(context)
interp = ""
interp = request(context)
print(interp)
pyperclip.copy(interp)
pyperclip.paste()
"""