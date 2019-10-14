from django.urls import path, include
from .views import register, profile


urlpatterns = [
    path('profile/', profile, name="profile"),
    path('register/', register, name="register"),
]