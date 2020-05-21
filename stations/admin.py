from django.contrib import admin

from stations.models import Station

class StationAdmin(admin.ModelAdmin):
    empty_value_display = '-vazio-'
    date_hierarchy = 'created_at' # Define quem vai ordenar
    ordering = ['-created_at'] # Define se a ordem é crescente ou decrescente
    list_display = ('name', 'stream_url', 'created_at', 'updated_at')
    list_display_links = ('name', 'stream_url')
    list_filter = ('name', 'stream_url')

admin.site.register(Station, StationAdmin)