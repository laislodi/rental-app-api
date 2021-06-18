from django.db import models

from api.apartment.model import Apartment


class ApartmentImage(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=200)
    favorite = models.BooleanField(default=False)
    apartment = models.ForeignKey(Apartment, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'apartment_images'
