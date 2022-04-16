from django.test import TestCase as DTestCase
from TimeToFly.auth_app.models import Profile, AppUser, AppUsersManager
from django.core.exceptions import ValidationError


class AppUserTests(DTestCase):
    VALID_USER_DATA = {
        'email': 'ilkothetiger@gmail.com',
        'password': 'n3m@DaTiKazh@',
        'pk': 1
    }

    def test_user_create_when_email_and_passowrd_are_acceptable__expect_success(self):
        user = AppUser(**self.VALID_USER_DATA)
        user.save()
        users = AppUser.objects.all()
        self.assertIsNotNone(users)

