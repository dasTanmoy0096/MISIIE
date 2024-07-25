from django.contrib import admin

# Register your models here.
from .models import Cppp, Gem, Offline

admin.site.register(Cppp)
admin.site.register(Gem)
admin.site.register(Offline)