# Generated by Django 4.0.3 on 2022-04-16 01:48

import TimeToFly.web.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_alter_flight_flight_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_time',
            field=models.DateTimeField(validators=[TimeToFly.web.validators.MinDateValidator(datetime.datetime(2022, 4, 16, 4, 48, 19, 397847))]),
        ),
    ]