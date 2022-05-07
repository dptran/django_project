from django.urls import path, include
from .views import TasklistView, DetailView


urlpatterns = [
    path('', TasklistView.as_view(), name='tasklist'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
]