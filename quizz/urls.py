from django.urls import path
from . import views
app_name = 'quizz'

urlpatterns = [
    path('index', views.index, name='index'),
    path('question', views.question, name='question'),
    path('response', views.response, name='response')
]