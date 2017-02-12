from django.db import models
from django import forms

# Create your models here.

class Anceator(models.model):
    first_name = models.CharField(max_length=24)
    secound_name = models.CharField(max_length=24, null = True)
    surname = models.CharField(max_length=36)
    maiden_name = models.CharField(max_length=36)
    relationship = models.ManyToManyField('relationship', through='AnceatorRelationship')

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.secound_name, self.surname)

class Relationship(models.Model):
    pass