from django.contrib import admin
from .models import Venue
from .models import MyUser
from .models import Event

# Register your models here.

admin.site.register(Venue)
admin.site.register(MyUser)
admin.site.register(Event)
