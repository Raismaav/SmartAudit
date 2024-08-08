from django.db import models

# Create your models here.
# models.py
from django.db import models

class Prueba(models.Model):
    date = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    rfc = models.CharField(max_length=255)
    guide = models.CharField(max_length=255)
    invoice = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    supplier = models.CharField(max_length=255)
    part_number = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    measure = models.CharField(max_length=255)
    fraction = models.CharField(max_length=255)
    unit_weight = models.CharField(max_length=255)
    total_weight = models.CharField(max_length=255)
    gross_weight = models.CharField(max_length=255)
    unit_value = models.CharField(max_length=255)
    total_value = models.CharField(max_length=255)
    incoterm = models.CharField(max_length=255)