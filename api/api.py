import requests
import json 

def fetchApi():
    res = requests.get('https://the-trivia-api.com/api/questions')
    response = json.loads(res.text)
    return response
