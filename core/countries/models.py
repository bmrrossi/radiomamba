from django.db import models
from django.utils import timezone

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    flag = models.FileField(upload_to='uploads/flags')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name