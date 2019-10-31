"""ms4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from home.urls import urlpatterns as index_pat
from accounts.urls import urlpatterns as acc_pat
from products.urls import urlpatterns as prod_pat
from search.urls import urlpatterns as search_pat
from cart.urls import urlpatterns as cart_pat
from .settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(index_pat), name="index"),
    path('accounts/', include(acc_pat)),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('products/', include(prod_pat)),
    path('search/', include(search_pat)),
    path('cart/', include(cart_pat)),
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': MEDIA_ROOT}),
]
