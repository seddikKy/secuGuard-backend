from django.contrib import admin

from .models import *


# Register your models here.
admin.site.register(Enterprise)
admin.site.register(TagHeader)
admin.site.register(TagDetail)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('designation', 'enterprise')
    ordering = ('designation',)
    search_fields = ('designation','enterprise',)

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('designation', 'site')
    ordering = ('designation',)
    search_fields = ('designation','site',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('designation', 'site')
    ordering = ('designation',)
    search_fields = ('designation','site',)