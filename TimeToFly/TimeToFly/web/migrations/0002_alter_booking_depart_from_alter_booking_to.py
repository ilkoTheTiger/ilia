# Generated by Django 4.0.3 on 2022-04-09 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='depart_from',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='booking',
            name='to',
            field=models.CharField(max_length=25),
        ),
    ]
