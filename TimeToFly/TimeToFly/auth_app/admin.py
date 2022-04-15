from django.contrib import admin
from TimeToFly.auth_app.models import AppUser, Profile

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Profile)