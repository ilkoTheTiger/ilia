# Generated by Django 4.0.3 on 2022-04-16 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_alter_flight_flight_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_time',
            field=models.DateTimeField(),
        ),
    ]
