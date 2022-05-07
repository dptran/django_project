from django import forms
from .models import Inquiry

class FormInquiry(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["first_name", "last_name", "email_address", "description"]
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email_address': 'Email',}