from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from api.api import fetchApiQuestions, categories, nextQuestion

saveQuestionResponse = {}
saveOptions = {}

#pageChoicesOptions
def index(request):
  
  template = loader.get_template('pageChoicesOptions.html')
  context = {
    'options': categories()
  }
  return HttpResponse(template.render(context,request))

#pageQuestions
def question(request, question):
  
  if 'next' in request.POST.keys()  :
    dataQuestion = nextQuestion()
    mixedResponses = []
    
    for datas in dataQuestion.items() :
      if datas[0] == 'correctAnswer' :
        mixedResponses.append(datas[1])
      if datas[0] == 'incorrectAnswers' :
        for responses in datas[1] :
          mixedResponses.append(responses)
  else :
    
    dataQuestion = fetchApiQuestions(request.POST)
    mixedResponses = []
    
    for datas in dataQuestion.items() :
      if datas[0] == 'correctAnswer' :
        mixedResponses.append(datas[1])
      if datas[0] == 'incorrectAnswers' :
        for responses in datas[1] :
          mixedResponses.append(responses)
          
  template = loader.get_template('pageQuestions.html')
  context = {
    'displayQuestion': dataQuestion,
    'choicesResponses': mixedResponses
  }
  return HttpResponse(template.render(context,request))

#pageResponse
def response(request, response):
  
  template = loader.get_template('pageResponse.html')
  context = {
    'response' : ""
  }
  return HttpResponse(template.render(context,request))

