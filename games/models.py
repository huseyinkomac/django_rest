from django.db import models


# Create your models here.
class Game(models.Model):
    '''
    Game Model
    @name - Name of the game in string
    @genre - Genre of the game in string
    @release_date - Release date of the game in date format
    '''
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_date = models.DateField()
