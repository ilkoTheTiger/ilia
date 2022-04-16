import django.utils.timezone
from django.test import TestCase as DTestCase
from django.shortcuts import reverse
from TimeToFly.web.models import Flight
from TimeToFly.auth_app.models import AppUser


class CreateFlightTests(DTestCase):
    def test_check_if_flight_is_created__expect_success(self):
        profile = AppUser(email='ilkothetiger@gmail.com', password='nemaDat1kaj@')
        profile.save()

        Flight(1, 'ABCDEF', "Sofia", 'London', 1, 300, django.utils.timezone.now())

        self.assertIsNotNone(Flight.objects.all())