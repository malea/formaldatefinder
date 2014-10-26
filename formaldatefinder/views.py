from django.http import HttpResponse
from django.shortcuts import render
from os import getenv

def index(request):
    context = {
        'fb_app_id': getenv('FB_APP_ID')
    }
    return render(request, 'index.html', context)

def register(request):
    return render(request, 'register.html')

def upcoming(request):
    return render(request, 'upcoming.html')


