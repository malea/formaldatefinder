from django.db import models
from django.forms import ModelForm

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=144)
    event_date = models.DateField()
    sponsor = models.CharField(max_length=144)
    location = models.CharField(max_length=144)

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_date', 'sponsor', 'location']


