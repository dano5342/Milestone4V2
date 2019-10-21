from django.urls import path, re_path
from .views import more_info


urlpatterns = [
    re_path(r'^(?P<product_id>\d+)/$', more_info, name="more info")
]
