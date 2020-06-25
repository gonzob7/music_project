# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=100)
    birth_city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=50)
    date_published = models.DateField()
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    date_published = models.DateField()
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    albums = models.ManyToManyField(Album, null=True)

    def __str__(self):
        return self.title
