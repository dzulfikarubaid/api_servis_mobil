from django.contrib import admin
from api.models import Servis

class ServisAdmin(admin.ModelAdmin):
    pass

admin.site.register(Servis,ServisAdmin)