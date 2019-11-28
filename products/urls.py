from django.urls import path, re_path
from .views import  all_products, MoreInfo


urlpatterns = [
    path('', all_products, name="products"),
    re_path(r'^(?P<category>[-\w]+)/$', all_products, name="products"),
    path('more_info/<int:pk>', MoreInfo.as_view(), name="more info")
]
