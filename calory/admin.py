from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.register(Food)
admin.site.register(Consume)
# Register your models here.
