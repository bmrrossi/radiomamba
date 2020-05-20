from django.db import models
from django.utils import timezone

# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=100)
    stream_url = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)