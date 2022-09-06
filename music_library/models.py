from unittest.util import _MAX_LENGTH
from django.db import models


class Music(models.model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_date = models.DateField()
    genre = models.CharField(max_length=25) 