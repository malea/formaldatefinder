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


    # Handle requests of type 'User', which save user objects to the DB
    if request.POST.get('type') == 'User':
        id_ = str(request.POST.get('fid'))
        try:
            u = User.objects.get(fid = id_)

        except:
            u = User(fid=id_)
            u.save()

    return HttpResponse(request)
