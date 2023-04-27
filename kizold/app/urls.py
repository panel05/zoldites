from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bejegyzesek/', views.bejegyzesek, name='bejegyzesek'),
    path('bejegyzesek/<int:osztaly_id>', views.bejegyzesekOsztalyId, name='bejegyzesekOsztalyId')
]