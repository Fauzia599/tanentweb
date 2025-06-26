from django.contrib import admin
from .models import *

# Register all models here
admin.site.register(User)
admin.site.register(TentCategory)
admin.site.register(Event)
admin.site.register(Booking)
admin.site.register(Payment)
