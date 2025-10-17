from django.urls import path
from .views import AboutList, ExhibitionList, about_create, about_edit

urlpatterns = [
    path('', AboutList.as_view(), name='about'),
    path('exhibitions/', ExhibitionList.as_view(), name='exhibitions'),
    path('new/', about_create, name='about_create'),
    path('<int:pk>/edit/', about_edit, name='about_edit'),
]