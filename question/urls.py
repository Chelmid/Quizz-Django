from django.urls import path
from . import views
app_name = 'quizz'

urlpatterns = [
    path('', views.index, name='index'),
    path('<question>', views.question, name='question'),
    path('question/<response>', views.response, name='response')
]