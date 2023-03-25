from django.urls import path
from . import views

urlpatterns = [
    path('dodaj_fiszke/', views.dodaj_fiszke),
    path('testuj/', views.rozpocznij_quiz),
    path('', views.dodaj_fiszke()),
]
