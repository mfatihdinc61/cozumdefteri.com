"""cozumdefteri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import sys

from django.template.context_processors import static


sys.path.append("..")  # Adds higher directory to python modules path.

from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views


from mebsci.views import custom_login, custom_register
from profil.views import profil
from gonderiyaz.views import create_post, gonderiler, post_detail, edit_post
# from mebsci.views import custom_register
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kayitol/', custom_register, name='kayitol'),
    path('', custom_login, name='login'),
    path('profil/', profil, name='profil'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('gonderiyaz/', create_post, name='gonderiyaz'),
    path('gonderiYaz/', create_post, name='gonderiyaz'),
    # path('ckeditor/', include('ckeditor_uploader.urls')),  # Add this line, commented for the next row
    re_path(r'^ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    re_path(r'^ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),
    path('gonderiler/', gonderiler, name='gonderiler'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('edit_post/<int:pk>/', edit_post, name='edit_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)