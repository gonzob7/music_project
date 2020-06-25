# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    context = {
        'musicians': Musician.objects.all()
    }
    return render(request, 'home.html', context)

def detail(request, musician_id):
    context = {
        'musician': Musician.objects.get(id=musician_id),
        'albums': Album.objects.all()
    }
    return render(request, 'detail.html', context)

def album_detail(request, album_id):
    context = {
        'album': Album.objects.get(id=album_id),
        'songs': Song.objects.all()
    }
    return render(request, 'album_detail.html', context)
