from django.contrib import admin

from .models import Status, Service, UserProfile 


admin.site.register(Service)
admin.site.register(UserProfile)

