from django.http import HttpResponse
from django.shortcuts import render
from os import getenv

from formaldatefinder.models import EventForm
from formaldatefinder.models import Event

def index(request):
    context = {
        'fb_app_id': getenv('FB_APP_ID')
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        f = EventForm(request.POST)
        new_event = f.save()
        #return render(request, 'register.html') 
    return render(request, 'register.html')

def upcoming(request):
    context = {
        'all_events' : Event.objects.all().order_by('-event_date')
    }
    return render(request, 'upcoming.html', context)

def event(request, event_id):

    # Query the database for this event
    try:
        e = Event.objects.get(id=event_id)

    # If the event does not exist, exit gracefully
    except Event.DoesNotExist:
        return HttpResponse("Event {} does not exist".format(
            event_id))

    return HttpResponse("looking at event {}".format(e.id))
