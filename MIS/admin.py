from django.contrib import admin

# Register your models here.
from .models import Cppp
from .models import Gem

admin.site.register(Cppp)
admin.site.register(Gem)