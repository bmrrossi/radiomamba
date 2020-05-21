from django.contrib import admin

from core.countries.models import Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

admin.site.register(Country, CountryAdmin)
