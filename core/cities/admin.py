from django.contrib import admin

from core.cities.models import City

class CityAdmin(admin.ModelAdmin):
    empty_value_display = '-vazio-'
    actions_on_top = True
    actions_on_bottom = False
    date_hierarchy = 'created_at' # Define quem vai ordenar
    ordering = ['-created_at'] # Define se a ordem é crescente ou decrescente
    list_display = ('name', 'state', 'created_at', 'updated_at')
    list_display_links = ('name', 'state')

admin.site.register(City, CityAdmin)