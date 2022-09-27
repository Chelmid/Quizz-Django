import requests
import json
import random

def fetchApiQuestions(request):
    
    categories = []
    difficulty = ''
    limit = ""
    apiURL = ""
    
    for datas in request.items() :
        if datas[1] == "on" :
            categories.append(datas[0])
        else : 
            if datas[0] == 'level' :
                difficulty = datas[1]
            if datas[0] == 'limit' :
                limit = datas[1]
    
    if len(categories) < 0 and difficulty == "":
        apiURL = "?limit=" + limit
    else : 
        if difficulty != "" :
            apiURL = "?categories=" + (",".join(categories)) + '&limit=' + limit + '&difficulty=' + difficulty
        else :
            apiURL = "?categories=" + (",".join(categories)) + '&limit=' + limit
    
    res = requests.get('https://the-trivia-api.com/api/questions' + apiURL)
    
    response = json.loads(res.text)
    
    return response[random.randint(0, len(response))]

def categories():
    tab = {}
    res = requests.get('https://the-trivia-api.com/api/categories')
    response = json.loads(res.text)
    
    for resultat in response :
        for value in response[resultat] : 
            if len(response[resultat]) <= 1 : 
                    tab.update({resultat : value })
            else : 
                if value.find('and') != -1 :
                    tab.update({resultat : value })
                    
    return tab