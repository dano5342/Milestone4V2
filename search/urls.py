from django.conf.urls import re_path
from .views import search


urlpatterns = [
    re_path(r'^$', search, name="search")
]