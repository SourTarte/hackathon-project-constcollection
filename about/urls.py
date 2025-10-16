from django.urls import path
from .views import AboutList, ExhibitionList

urlpatterns = [
    path('', AboutList.as_view(), name='about'),
    path('exhibitions/', ExhibitionList.as_view(), name='exhibitions'),
]