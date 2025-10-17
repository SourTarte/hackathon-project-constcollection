"""
URL configuration for constcollection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.art_list, name='art_list')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='art_list')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gallery import views as gallery_views

urlpatterns = [
    path('', gallery_views.welcome_view, name='welcome'),
    path('gallery/', gallery_views.art_view, name='art'),
    path('adminpanel/', gallery_views.admin_view, name='admin_panel'),
    path('about/', include("about.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include("allauth.urls")),
]
