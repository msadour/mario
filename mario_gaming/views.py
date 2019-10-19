from django.shortcuts import render
from .models import Mario, Princess, Game


def home(request):
    return render(request, 'mario_gaming/home.html')

def move_mario(request):
    pass

def solutions(request):
    pass

