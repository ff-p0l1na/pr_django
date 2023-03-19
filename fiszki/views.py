from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormularzDodawniaFiszek


def dodaj_fiszke(request):
    form = FormularzDodawniaFiszek
    return render(request, 'fiszki/dodaj_fiszke.html', {'form': form})


def rozpocznij_quiz(request):
    return HttpResponse("Praca w toku.")
