from django.urls import path
from .views import SignUpView, ProfileView, LocationForm, UserForm

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path("locations/", LocationForm.as_view(), name="locations"),
    path("users/", UserForm.as_view(), name="users"),
    path("signup/", SignUpView.as_view(), name="signup"),
]