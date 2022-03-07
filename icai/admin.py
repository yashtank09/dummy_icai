from django.contrib import admin
from .models import icai_registration, student_questions

# Register your models here.
@admin.register(icai_registration)
class RegIcai(admin.ModelAdmin):
    list_display = ['register_id', 'usericai_region', 'membershipicai_id', 'username_icai', 'user_email_icai', 'user_contact_icai']

@admin.register(student_questions)
class StudQus(admin.ModelAdmin):
    list_display = []