import requests
import json 

def fetchApiQuestions():
    res = requests.get('https://the-trivia-api.com/api/questions')
    #https://the-trivia-api.com/api/questions?categories=arts_and_literature&limit=5&difficulty=medium&tags=1930's
    response = json.loads(res.text)
    return response

def categories():
    tab = []
    res = requests.get('https://the-trivia-api.com/api/categories')
    response = json.loads(res.text)
    #print(response)
    for resultat in response :
        for value in response[resultat] : 
            if len(response[resultat]) <= 1 : 
                   tab.append({response[resultat] : value})
            else : 
                if value.find('and') != -1 :
                    tab.append({response[resultat] : value})
                
    print(tab)
    return response