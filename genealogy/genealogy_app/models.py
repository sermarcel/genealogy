from django.db import models
from django import forms

# Create your models here.


RELATION_TYPES = (
    (-1, "nie określono"),
    (0, "syn"),
    (1, "córka"),
    (2, "ojciec"),
    (3, "matka"),
    (4, "brat"),
    (5, "siostra"),
    (6, "partner")

)

GENDER = (
(-1, "nie określono"),
    (0, "kobieta"),
    (1, "mężczyzna")
)


DEAD_OR_ALIVE = (
(-1, "nie określono"),
    (0, "żyje"),
    (1, "nie żyje")
)


class Family(models.Model):
    family_name = models.CharField(max_length=24)

    def __str__(self):
        return '{}'.format(self.family_name)

class Anceator(models.Model):
    first_name = models.CharField(max_length=24)
    secound_name = models.CharField(max_length=24, null=True, blank=True)
    surname = models.CharField(max_length=36)
    gender = models.IntegerField(choices=GENDER, default=-1)
    maiden_name = models.CharField(max_length=36, null=True, blank=True)
    #relationship = models.ManyToManyField('relationship', through='AnceatorRelationship')
    family = models.ForeignKey(Family, default='')
    notes = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='static/content/', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    dead_or_alive = models.IntegerField(choices=DEAD_OR_ALIVE, default=-1)    
    death_date = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.secound_name, self.surname)
'''
class Relationship(models.Model):
    relation_name = models.IntegerField(choices=RELATION_TYPES, default=-1)
    anceator = models.ForeignKey(Anceator, on_delete=models.CASCADE,related_name='anceator1' )
    family = models.ForeignKey(Anceator, on_delete=models.CASCADE, related_name='anceator2')
        
    def __str__(self):
        return '{}  is {} for {}'.format(self.anceator, self.relation_name, self.family)
'''

