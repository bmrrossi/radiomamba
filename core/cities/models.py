from django.db import models
from django.utils import timezone

from core.countries.models import Country

# Create your models here.

class Cities(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.ForeignKey(Country)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)