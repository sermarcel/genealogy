from django.db import models
from django import forms

# Create your models here.


RELATION_TYPES = (
    (-1, "nie określono"),
    (0, "rodzic"),
    (1, "dziecko"),
    (2, "rodzeństwo"),
    (3, "w związku")

)


class Anceator(models.Model):
    first_name = models.CharField(max_length=24)
    secound_name = models.CharField(max_length=24, null = True)
    surname = models.CharField(max_length=36)
    maiden_name = models.CharField(max_length=36)
    relationship = models.ManyToManyField('relationship', through='AnceatorRelationship')
    notes = models.TextField()
    image = models.ImageField(upload_to='static/content/', null=True, blank=True)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.secound_name, self.surname)

class Relationship(models.Model):
    relation_name = models.IntegerField(choices=RELATION_TYPES, default=-1)

class AnceatorRelationship(models.Model):
    relationship = models.ForeignKey(Relationship)
    anceator = models.ForeignKey(Anceator)