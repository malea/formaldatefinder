from django.http import HttpResponse
from django.shortcuts import render
from os import getenv

from formaldatefinder.models import EventForm

def index(request):
    context = {
        'fb_app_id': getenv('FB_APP_ID')
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        f = EventForm(request.POST)
        new_event = f.save()
        return HttpResponse('Saved to Database!')
    return render(request, 'register.html')

def upcoming(request):
    return render(request, 'upcoming.html')


