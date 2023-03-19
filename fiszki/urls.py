from django.urls import path
from fiszki import views

urlpatterns = [
    path('dodaj_fiszke/', views.dodaj_fiszke),
    path('testuj/', views.rozpocznij_quiz),
]
