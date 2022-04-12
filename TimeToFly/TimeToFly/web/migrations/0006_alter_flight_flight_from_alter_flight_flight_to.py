# Generated by Django 4.0.3 on 2022-04-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_flight_flight_from_alter_flight_flight_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_from',
            field=models.CharField(choices=[(5, 'Sofia'), (6, 'Berlin'), (7, 'London'), (8, 'Reading'), (9, 'New Town'), (10, 'New York')], max_length=30),
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_to',
            field=models.CharField(choices=[(5, 'Sofia'), (6, 'Berlin'), (7, 'London'), (8, 'Reading'), (9, 'New Town'), (10, 'New York')], max_length=30),
        ),
    ]