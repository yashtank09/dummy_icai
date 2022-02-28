from django import forms
from icai.models import icai_icai_registration


class IcaiRegistration(forms.ModelForm):
    class Meta:
        model = icai_icai_registration
        # fields = ['usericai_region', 'membershipicai_id', 'username_icai', 'user_email_icai', 'user_contact_icai']
        fields = "__all__"