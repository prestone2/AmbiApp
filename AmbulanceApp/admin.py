from django.contrib import admin

from AmbulanceApp.models import User
from AmbulanceApp.models import Ambulance

# Register your models here.

admin.site.register(User)
admin.site.register(Ambulance)

