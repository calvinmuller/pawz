from django.contrib import admin

# Register your models here.
from .models import Organisation, Status


class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'address', 'owner', 'status', 'image_tag')
    fieldsets = [
        (None, {'fields': ['name', 'slug', 'address', 'owner', 'can_donate', 'featured', 'image', 'status']})
    ]
    list_filter = ['date_created']

class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    fieldsets = [
        (None, {'fields': ['name']})
    ]
    list_filter = ['name']


admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Status, StatusAdmin)

