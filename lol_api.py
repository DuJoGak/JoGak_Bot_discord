import token_private
import requests
import json

def lol_read(nickname):
    r=requests.get('https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+str(nickname)+'?api_key='+str(token_private.Lol_api_Key))
    data=json.loads(r.text)
    enid=data['']
    return data
    print(data)