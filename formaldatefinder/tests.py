from django.test import TestCase
from formaldatefinder.models import Event
from datetime import date


class EventTestCase(TestCase):

    def setUp(self):
        """
        Create Event objects to use with testing. The first event has
        already happened, and the second Event is upcoming.
        """
        Event.objects.create(
            event_name="Black Diamond",
            event_date=date(2001, 9, 11),
            sponsor="FIJI",
            location="Electric Ave."
        )

        Event.objects.create(
            event_name="WhyYouMufasa",
            event_date=date(3005, 1, 1),
            sponsor="Glover, Donald",
            location="Mars"
        )

    def test_upcoming(self):
        """
        The old event is not upcoming.
        The upcoming event is upcoming.
        """
        old_event = Event.objects.get(id=1)
        upcoming_event = Event.objects.get(id=2)

        self.assertFalse(old_event.is_upcoming())
        self.assertTrue(upcoming_event.is_upcoming())
