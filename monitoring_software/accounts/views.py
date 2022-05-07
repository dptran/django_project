from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, LocationForm, UserForm
from .models import CustomUser, Location


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ProfileView(CreateView):
    model = CustomUser
    fields = '__all__'
    success_url = reverse_lazy("user_profile")
    template_name = 'user_profile.html'


class LocationForm(CreateView):
    form_class = LocationForm
    success_url = reverse_lazy("add_location")
    template_name = "add_location.html"


class UserForm(CreateView):
    form_class = UserForm
    success_url = reverse_lazy("add_user")
    template_name = "add_user.html"
