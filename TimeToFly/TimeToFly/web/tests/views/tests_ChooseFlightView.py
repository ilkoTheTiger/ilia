import django.utils.timezone
from django.test import TestCase as DTestCase
from django.shortcuts import reverse
from TimeToFly.web.models import Passenger, Flight
from TimeToFly.auth_app.models import AppUser
from django.core.exceptions import ValidationError



class ChooseFlightTests(DTestCase):
    def test_check_if_flight_is_chosen__expect_success(self):
        profile = AppUser(email='ilkothetiger@gmail.com', password='nemaDat1kaj@')
        profile.save()

        Flight(1, 'ABCDEF', "Sofia", 'London', 1, 300, django.utils.timezone.now())

        Passenger(1)

        response = self.client.get(reverse('book flight'))

        self.assertIsNotNone(Passenger.objects.all())

    def test_check_if_rejects_nunselected_booking_attempts__expect_to_fail(self):
        profile = AppUser(email='ilkothetiger@gmail.com', password='nemaDat1kaj@')
        profile.save()

        Flight(1, 'ABCDEF', "Sofia", 'London', 1, 300, django.utils.timezone.now())

        booking = Passenger()

        response = self.client.get(reverse('book flight'))

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
            booking.full_clean()
            booking.save()

        self.assertIsNotNone(context.exception)

    def test_check_if_2_people_can_book_the_same_flight__expect_success(self):
        profile1 = AppUser(email='ilkothetiger@gmail.com', password='nemaDat1kaj@')
        profile1.save()
        profile2 = AppUser(email='iliadimchev@gmail.com', password='nemaDat1kaj@')
        profile2.save()


        Flight(1, 'ABCDEF', "Sofia", 'London', 1, 300, django.utils.timezone.now())

        booking1 = Passenger(1)
        booking1.save()
        booking2 = Passenger(2)
        booking2.save()

        response = self.client.get(reverse('book flight'))
        self.assertIsNotNone(Passenger.objects.all())
