from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from api.api import fetchApiQuestions, categories

def index(request):
  
  template = loader.get_template('PageChoices.html')
  context = {
    'categories': categories()
  }
  return HttpResponse(template.render(context,request))


def id(request, question_id):
  
  print(request.POST)
  
  template = loader.get_template('PageQuestions.html')
  context = {
    'questions': fetchApiQuestions(),
  }
  return HttpResponse(template.render(context,request))

