from django.db import models


class AboutUs(models.Model):
    id = models.AutoField(primary_key=True)
    html = models.TextField(max_length=131070)

    class Meta:
        db_table = 'about_us'


class Parameters(models.Model):
    id = models.AutoField(primary_key=True)
    contact_telephone_number = models.CharField(max_length=25)
    facebook_link = models.CharField(max_length=200)
    facebook_text = models.CharField(max_length=200)
    instagram_link = models.CharField(max_length=200)
    instagram_text = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=150, null=False)

    class Meta:
        db_table = 'parameters'
