from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=25)
    weight=models.IntegerField()
    price=models.IntegerField()
    created_at=models.DateField()
    updated_at=models.DateTimeField(default=timezone.now)
