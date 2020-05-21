from django.db import models
from django.utils import timezone

from core.countries.models import Country

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name