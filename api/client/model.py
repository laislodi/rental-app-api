from django.db import models
from ..apartment.model import Apartment
from ..state.model import State


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    rg_number = models.CharField(max_length=12)
    # By default, Django populates column's name by appending _id to the field name you define
    # in your model. You must explicitly specify column's name using db_column property
    rg_state = models.ForeignKey(State, db_column='rg_state', on_delete=models.DO_NOTHING)
    cpf = models.CharField(max_length=11)
    apartment = models.ForeignKey(Apartment, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'client'
