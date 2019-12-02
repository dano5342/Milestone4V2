from .views import index, about, jobs, contact
from django.urls import path, re_path


urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('jobs/', jobs, name="jobs"),
    path('contact/', contact, name="contact")
]
