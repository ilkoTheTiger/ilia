from django.test import TestCase as DTestCase
from TimeToFly.auth_app.models import Profile, AppUser
from django.core.exceptions import ValidationError


class ProfileTests(DTestCase):
    VALID_PROFILE_DATA = {
        'first_name': 'Ilia',
        'last_name': 'Dimchev',
        'age': 26,
        'passport': 159753486,
        'pk': 1,
    }

    VALID_USER_DATA = {
        'id': 1,
        'email': 'ilkothetiger@gmail.com',
        'password': 'N3kF@par0LA',
    }

    def test_profile_create_when_name_are_only_letters_and_appropriate_length__expect_success(self):
        user = AppUser(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_create_when_first_name_contains_a_digit__expect_to_fail(self):
        first_name = 'Ilia1'
        user = AppUser(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            age=self.VALID_PROFILE_DATA['age'],
            passport=self.VALID_PROFILE_DATA['passport'],
            user_id=self.VALID_PROFILE_DATA['pk']
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create_when_first_name_contains_a_dollar__expect_to_fail(self):
        first_name = 'Ilia%'
        user = AppUser(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            age=self.VALID_PROFILE_DATA['age'],
            passport=self.VALID_PROFILE_DATA['passport'],
            user_id=self.VALID_PROFILE_DATA['pk']
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create_when_first_name_contains_a_hashtag__expect_to_fail(self):
        first_name = 'Ilia#'
        user = AppUser(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            age=self.VALID_PROFILE_DATA['age'],
            passport=self.VALID_PROFILE_DATA['passport'],
            user_id=self.VALID_PROFILE_DATA['pk']
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_rejects_passport_different_than_9_digits(self):
        passport = 456654
        user = AppUser(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(
            first_name=self.VALID_PROFILE_DATA['first_name'],
            last_name=self.VALID_PROFILE_DATA['last_name'],
            age=self.VALID_PROFILE_DATA['age'],
            passport=passport,
            user_id=self.VALID_PROFILE_DATA['pk']
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)