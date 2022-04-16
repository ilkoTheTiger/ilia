# Generated by Django 4.0.3 on 2022-04-16 02:11

import TimeToFly.web.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0011_alter_profile_passport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), TimeToFly.web.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), TimeToFly.web.validators.validate_only_letters]),
        ),
    ]