from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Location, User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name")


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name", "address", "city", "state", "zip", "capacity", "description"]
        labels = {"name": "Name", "address": "Address", "city": "City", "state": "State", "zip": "Zip Code", "capacity": "Capacity", "description":"Description"}


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "phone", "notes"]
        labels = {"name": "Full Name", "email": "Email Address", "phone": "Phone Number", "notes": "Additional Notes"}
