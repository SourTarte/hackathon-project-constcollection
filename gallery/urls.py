from . import views
from django.urls import path

urlpatterns = [
    path('', views.art_view, name='welcome'),
]
