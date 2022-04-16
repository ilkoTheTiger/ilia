import datetime

import django.utils.timezone
from django.test import TestCase as DTestCase
from django.shortcuts import reverse
from TimeToFly.web.models import Flight
from TimeToFly.auth_app.models import AppUser
from django.core.exceptions import ValidationError


class FlightTest(DTestCase):
    VALID_PROFILE_DATA = {
        'first_name': 'Ilia',
        'last_name': 'Dimchev',
        'age': 26,
        'passport': 159753486,
        'pk': 1,
    }

    def test_get_renders_correct_template(self):
        response = self.client.get(reverse('show flights'))

        self.assertTemplateUsed(response, 'flights-list.html')

    def test_get__when_3_flights__expect_context_to_contain_3_flights(self):
        profile = AppUser(email='ilkothetiger@gmail.com', password='nemaDat1kaj@')
        profile.save()

        flights_to_create = (
            Flight(1, 'ABCDEF', "Sofia", 'London', 1, 300, django.utils.timezone.now()),
            Flight(2, 'ABGDEF', "Sofia", 'Berlin', 1, 400, django.utils.timezone.now()),
            Flight(3, 'AWCDEF', "Berlin", 'London', 1, 500, django.utils.timezone.now()),
        )
        Flight.objects.bulk_create(flights_to_create)

        response = self.client.get(reverse('show flights'))

        flights = response.context['object_list']
        self.assertEqual(len(flights), 3)
