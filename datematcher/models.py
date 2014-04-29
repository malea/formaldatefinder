from django.db import models

class UserProfile(models.Model):
    looking_for_formal = models.BooleanField(default=True)

class Formal(models.Model):
    event_date = models.DateField()
    sponsor = models.CharField(max_length=144)
    location = models.CharField(max_length=144, null=True, blank=True)

    host = models.ForeignKey(UserProfile)
    date_found = models.BooleanField(default=False)
