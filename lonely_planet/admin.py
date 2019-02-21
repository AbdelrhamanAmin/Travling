from django.contrib import admin
from .models import *
from blogapp.models import *
# Register your models here.
admin.site.register(customUser)

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Location)
admin.site.register(Hotel)