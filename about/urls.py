from django.urls import path
from .views import AboutList, ExhibitionList, about_create

urlpatterns = [
    path('', AboutList.as_view(), name='about'),
    path('exhibitions/', ExhibitionList.as_view(), name='exhibitions'),
    path('new/', about_create, name='about_create'),
]