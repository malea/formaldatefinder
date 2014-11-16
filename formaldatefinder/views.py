from django.http import HttpResponse
from django.shortcuts import render
from os import getenv

from django.views.decorators.csrf import csrf_exempt

from formaldatefinder.models import EventForm, Event, User

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

    context = {
            'id': e.id,
            'name' : e.event_name,
            'date' : e.event_date, 
            'sponsor' : e.sponsor, 
            'location' : e.location
            }
    return render(request, 'event.html', context)

@csrf_exempt
def api(request):

    if request.method != 'POST':
        return HttpResponse('POST requests only')

    fid_ = str(request.POST.get('fid'))
    eid_ = str(request.POST.get('eid'))

    # Get the appropriate Event object
    e = Event.objects.get(id=eid_)

    # Add the user as an attendee to the event
    u = User(fid=fid_)
    u.event = e
    u.save()

    return HttpResponse(request)
