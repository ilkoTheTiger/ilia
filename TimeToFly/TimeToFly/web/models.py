from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.contrib import admin
from TimeToFly.auth_app.models import AppUser
from django.core.exceptions import ValidationError


class Town(models.Model):

    TOWN_MAX_LEN = 187

    town = models.CharField(
        max_length=TOWN_MAX_LEN,
    )

    def __str__(self):
        return self.town

class Flight(models.Model):
    FLIGHT_MINIMUM_NUMBER = 0
    FLIGHT_CODE_MAX_LEN = 6
    FLIGHT_CODE_MIN_LEN = 6
    FLIGHT_FROM_MAX_LEN = 30
    FLIGHT_TO_MAX_LEN = 30
    DEFAULT_FLIGHT_PRICE = 0
    FLIGHT_MINIMUM_PRICE = 0

    flight_number = models.IntegerField(
        unique=True,
        primary_key=True,
        validators=(
            MinValueValidator(FLIGHT_MINIMUM_NUMBER),
        )
    )

    flight_code = models.CharField(
        max_length=FLIGHT_CODE_MAX_LEN,
        unique=True,
        validators=(
            MinLengthValidator(FLIGHT_CODE_MIN_LEN),
                    )
    )

    flight_from = models.CharField(
        max_length=FLIGHT_FROM_MAX_LEN,
        choices=((choice.town, choice.town) for choice in Town.objects.all()),
    )

    flight_to = models.CharField(
        max_length=FLIGHT_TO_MAX_LEN,
        choices=((choice.town, choice.town) for choice in Town.objects.all()),
    )

    def clean(self):
        if self.flight_from == self.flight_to:
            raise ValidationError('Flight From must be different than Flight To.')

    flight_cost = models.FloatField(
        default=DEFAULT_FLIGHT_PRICE,
        validators=(
            MinValueValidator(FLIGHT_MINIMUM_PRICE),
        )
    )

    flight_time = models.DateTimeField()

    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['flight_number']

    def __str__(self):
        return self.flight_code

class Passenger(models.Model):
    SELECTED_MAX_LEN = 287
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True
    )

    bookings = models.ManyToManyField(
        Flight,
        verbose_name="Available Flights"
    )

    def __str__(self):
        return str(self.user)


class Booking(models.Model):
    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    depart_from = models.CharField(
        max_length=25
    )

    to = models.CharField(
        max_length=25
    )

    date = models.DateTimeField()

