# Generated by Django 4.0.3 on 2022-04-13 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_delete_airport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='bookings',
            field=models.ManyToManyField(to='web.flight', verbose_name='Available Flights'),
        ),
    ]
