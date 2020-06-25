# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Musician

# Create your views here.

def home(request):
    context = {
        'musicians': Musician.objects.all()
    }
    return render(request, 'home.html', context)

def detail(request, musician_id):
    context = {
        'musician': Musician.objects.get(id=musician_id)
    }
    return render(request, 'detail.html', context)
