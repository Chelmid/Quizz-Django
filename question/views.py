from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from api.api import fetchApiQuestions, categories

def index(request):
  
  template = loader.get_template('pageChoices.html')
  context = {
    'categories': categories()
  }
  return HttpResponse(template.render(context,request))


def question(request, question_id):
  
  template = loader.get_template('pageQuestions.html')
  context = {
    'question': fetchApiQuestions(request.POST),
  }
  return HttpResponse(template.render(context,request))

