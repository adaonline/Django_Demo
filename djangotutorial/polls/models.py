from django.db import models

# Create your models here.
class Questions(models.Model):
    questions_text = models.CharField(max_length=200)
    pub_date = models.DateField("data published")

class Choice(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)