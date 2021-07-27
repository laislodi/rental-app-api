from django.db import models

from api.apartment.model import Apartment


class Specifications(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=70, unique=True)
    apartment_id = models.ForeignKey(Apartment, on_delete=models.CASCADE())
