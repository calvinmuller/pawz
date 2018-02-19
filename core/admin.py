from django.contrib import admin

# Register your models here.
from .models import Organisation, Status, OrganisationImage, Paw, Breed, Colour, PawImage


class OrganisationbImageInline(admin.TabularInline):
    model = OrganisationImage
    extra = 0


class PawsImageInline(admin.TabularInline):
    model = PawImage
    extra = 0


class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'address', 'owner', 'status', 'logo', 'slug')
    fieldsets = [
        (None, {'fields': ['name', 'slug', 'address', 'owner', 'can_donate', 'featured', 'logo', 'status']})
    ]
    list_filter = ['date_created']
    readonly_fields = ['slug']
    inlines = [OrganisationbImageInline, ]


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    fieldsets = [
        (None, {'fields': ['name']})
    ]
    list_filter = ['name']


class PawAdmin(admin.ModelAdmin):
    list_select_related = ('breed', 'colour')
    list_display = ('name', 'slug', 'colour', 'breed', 'organisation', 'picture', 'status')
    fieldsets = [
        (None, {'fields': ['name', 'slug', 'organisation', 'picture']}),
        ('Information', {'fields': ['colour', 'breed', 'breed_other', 'can_adopt', 'can_donate', 'status']}),
        ('Favourites', {'fields': ['favourite_food', 'favourite_toy', ]}),
        ('Dates', {'fields': ['date_of_birth', 'adopted_at']})
    ]
    list_filter = (
        ('colour__name'),
        ('breed__name'),
    )
    readonly_fields = ['slug']
    inlines = [PawsImageInline, ]


class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    fields = ('name', 'image')


class ColourAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    fields = ('name', 'image')


admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Paw, PawAdmin)
admin.site.register(Breed, BreedAdmin)
admin.site.register(Colour, ColourAdmin)
