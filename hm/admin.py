from django.contrib import admin

from .models import Status, Service, UserProfile 
from django.utils.translation import ugettext_lazy


admin.site.site_title 	= ugettext_lazy('Highway Mechanic Super Admin')
admin.site.site_header 	= ugettext_lazy('Highway Mechanic')
admin.site.index_title 	= ugettext_lazy('Highway Mechanic Secure')

admin.site.register(Service)
admin.site.register(UserProfile)

