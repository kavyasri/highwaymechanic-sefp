from django.contrib import admin

from .models import Status,Mechanic,Driver,Service,Payment,ServiceLog

admin.site.register(Mechanic)
admin.site.register(Driver)
admin.site.register(Service)
admin.site.register(ServiceLog)

