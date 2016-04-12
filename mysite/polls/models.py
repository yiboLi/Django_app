from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model): #Each model is represented by a class that subclasses django.db.models.Model. 
    question_text = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #Each model has a number of class variables, each of which represents a database field in the model.
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # each Choice is related to a single Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) #default value
    def __str__(self):
        return self.choice_text