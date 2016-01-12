from django.db import models

# Python is running this in order so List comes before
class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default='')
    list= models.ForeignKey(List, default= None)
