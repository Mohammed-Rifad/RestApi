from django.db import models

# Create your models here.


class Course(models.Model):
    c_name=models.CharField(max_length=20)
    c_fee=models.FloatField()


class Trainer(models.Model):
    tr_name=models.CharField(max_length=20)
    tr_age=models.IntegerField()
    
        