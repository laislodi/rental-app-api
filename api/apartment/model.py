from django.db import models


class Apartment(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=4, unique=True)
    bedrooms = models.IntegerField()
    description = models.CharField(max_length=100)
    price = models.FloatField()
    available = models.BooleanField(default=True)
    highlighted = models.BooleanField(default=False)

    class Meta:
        db_table = 'apartment'

    def __str__(self):
        return self.number



