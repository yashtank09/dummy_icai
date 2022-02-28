from django.forms import ModelForm, Textarea
from django.db import models


# Create your models here.

class icai_icai_registration(models.Model):
    register_id = models.IntegerField()
    usericai_region = models.CharField(max_length=45)
    membershipicai_id = models.IntegerField()
    username_icai = models.CharField(max_length=80)
    user_email_icai = models.CharField(max_length=90)
    user_contact_icai = models.IntegerField()

    class Meta:
        db_table = 'icai_registration'
