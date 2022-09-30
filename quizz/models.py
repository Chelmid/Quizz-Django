from django.db import models

class UserName (models.Model) :
    name = models.CharField(max_length=200)
    date = models.DateField('date_create')
    scoreMax = models.IntegerField(default=0)
    
    def __str__(self) :
        return (self.name)