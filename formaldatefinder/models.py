from django.db import models
from django.forms import ModelForm
from datetime import date


class Event(models.Model):

    '''This model is the Event model.

    We store the name of the event, the date of the event,
    the sponsoring organization name, and the location
    of the event.'''
    event_name = models.CharField(max_length=144)
    event_date = models.DateField()
    sponsor = models.CharField(max_length=144)
    location = models.CharField(max_length=144)

    def is_upcoming(self):
        return self.event_date > date.today()


class EventForm(ModelForm):

    '''The Event Form allows a user to create a new event.

    The user must provide the name of the event, the date of
    the event, the sponsor of the event, and the location of
    the event.'''
    class Meta:
        model = Event
        fields = ['event_name', 'event_date', 'sponsor', 'location']


class User(models.Model):

    '''All we need to store in the database for the user is the fid.

    The fid is the unique string that identifies a unique user of
    Facebook.'''
    fid = models.CharField(max_length=144)
    event = models.ForeignKey(Event)