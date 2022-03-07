from datetime import datetime

from django.forms import ModelForm, Textarea
from django.db import models


# Create your models here.

class icai_registration(models.Model):
    register_id = models.IntegerField(primary_key=True)
    usericai_region = models.CharField(max_length=45, null=False)
    membershipicai_id = models.IntegerField(null=False)
    username_icai = models.CharField(max_length=80, null=False)
    user_email_icai = models.EmailField(max_length=90, null=False)
    user_contact_icai = models.BigIntegerField(null=False)


class student_questions(models.Model):
    current_time = datetime.now()
    # user_name = models.ForeignKey(icai_registration, on_delete=models.CASCADE)
    UserRegID = models.IntegerField(null=False)
    qus_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=80, null=False)
    user_question = models.CharField(max_length=300, null=False)
    question_datetime = models.DateTimeField(default=current_time, blank=True)
    # primary_key = True if you do not want to use default field "id" given by django to your model
