# Generated by Django 4.0.3 on 2022-04-07 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0007_alter_appuser_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='is_deleted',
        ),
    ]
