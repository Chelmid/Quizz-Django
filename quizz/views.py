from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from api.api import fetchApiQuestions, categories, nextQuestion
from .models import UserName

import random
import datetime

saveQuestionResponse = {}
saveResponse = ""
saveOptions = {}
counter = 0
limit = 0
score = 0

#pageChoicesOptions
def index(request):
  
  template = loader.get_template('pageChoicesOptions.html')
  context = {
    'options': categories()
  }
  return HttpResponse(template.render(context,request))

#pageQuestions
def question(request):
  
  global limit
  global counter
  global saveResponse
  global score
  
  mixedResponses = []
  
  if 'next' in request.POST.keys() :
    
    dataQuestion = nextQuestion()
    
    for datas in dataQuestion.items() :
      if datas[0] == 'correctAnswer' :
        mixedResponses.append(datas[1])
        saveResponse = datas[1]
      if datas[0] == 'incorrectAnswers' :
        for responses in datas[1] :
          mixedResponses.append(responses)
    counter += 1
    
  else :
    
    if(len(UserName.objects.filter(name=request.POST.get("name"))) > 0) :
      template = loader.get_template('pageChoicesOptions.html')
      context = {
        'messageError' : 'le pseudo est déjà utilisé'
      }
      return redirect('http://127.0.0.1:8000/quizz/index', messageError = "messageError")
    
    else :
      limit = (request.POST).get("limit")
      print(request.POST)
      dataQuestion = fetchApiQuestions(request.POST)
      
      # save = UserName(name=(request.POST).get("name"), date=datetime.datetime.now(),scoreMax=0 )
      # save.save()
      
      for datas in dataQuestion.items() :
        if datas[0] == 'correctAnswer' :
          mixedResponses.append(datas[1])
          saveResponse = datas[1]
        if datas[0] == 'incorrectAnswers' :
          for responses in datas[1] :
            mixedResponses.append(responses)
      counter += 1
    
  shuffle = random.sample(mixedResponses, len(mixedResponses))
  
  template = loader.get_template('pageQuestions.html')
  context = {
    'displayQuestion': dataQuestion,
    'choicesResponses': shuffle
  }
  return HttpResponse(template.render(context,request))

#pageResponse
def response(request):
  
  global limit
  global counter
  global score
  global saveResponse
  
  for key, value in request.POST.items() :
    if key == saveResponse:
      score += 1
  
  if int(limit) <= counter :
    template = loader.get_template('pageResult.html')
    limit = 0
    counter = 0
    context = {
      'response' : saveResponse,
      'score': score
    }
    return HttpResponse(template.render(context,request))
  
  else : 
    template = loader.get_template('pageResponse.html')
    context = {
      'response' : saveResponse,
      'score': score
    }
    return HttpResponse(template.render(context,request))

#pageResult
def result(request):
  global score
  score = 0
  
  template = loader.get_template('pageChoicesOptions.html')
  
  context = {
    'response' : ""
  }
  return HttpResponse(template.render(context,request))