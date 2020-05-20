from django.db import models
from django.utils import timezone

from core.cities.models import City

# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=100)
    stream_url = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name