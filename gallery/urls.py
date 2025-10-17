from . import views
from django.urls import path

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('gallery/', views.art_view, name='art_list'),
    
]
