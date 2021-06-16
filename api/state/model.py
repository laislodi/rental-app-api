from django.db import models


class State(models.Model):
    abbrev = models.CharField(primary_key=True, max_length=2)
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'state'
