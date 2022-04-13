from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
# from django.core.validators import MinValueValidator
# from django.core.exceptions import ValidationError
from TimeToFly.auth_app.managers import AppUsersManager
from TimeToFly.web.validators import MaxFileSize
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MinLengthValidator
from django.core.validators import deconstructible, ValidationError, MaxValueValidator


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,

    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    

    USERNAME_FIELD = 'email'

    objects = AppUsersManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 25
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 25
    LAST_NAME_MIN_LEN = 2
    AGE_MIN_VALUE=18
    PASSPORT_MIN_VALUE=100000000
    PASSPORT_ID_TOO_LONG_VALUE  = 999999999

    IMAGE_UPLOAD_DIR = 'images/'
    MAX_FILE_SIZE_IN_MEGABYTES = 5


    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(MinLengthValidator(FIRST_NAME_MIN_LEN),
    ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(MinLengthValidator(LAST_NAME_MIN_LEN),
    ),
    )

    age = models.IntegerField(
        validators=(MinValueValidator(AGE_MIN_VALUE),),
        null=True,
        blank=True,
    )

    passport = models.IntegerField(
        validators=(MinValueValidator(PASSPORT_MIN_VALUE, message = ("Ensure your Passport ID is 9 digits.")),
                    MaxValueValidator(PASSPORT_ID_TOO_LONG_VALUE, message = ("Ensure your Passport ID is 9 digits.")),
                    ),
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to=IMAGE_UPLOAD_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSize(MAX_FILE_SIZE_IN_MEGABYTES),
        )
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


@receiver(post_delete, sender=Profile)
def auto_delete_user_with_profile(sender, instance, **kwargs):
    instance.user.delete()