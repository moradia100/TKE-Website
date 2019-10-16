from django.contrib import admin

# Register your models here.
from .models import Event
from .models import Gallery
admin.site.register(Event)
admin.site.register(Gallery)
