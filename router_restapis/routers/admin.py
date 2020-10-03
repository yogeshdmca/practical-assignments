from django.contrib import admin
from routers.models import Router

# Register your models here.


@admin.register(Router)
class RouterAdmin(admin.ModelAdmin):
    list_display = ('id', 'loopback', 'hostname', 'ip')