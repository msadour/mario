from django.shortcuts import render


def home(request):
    return render(request, 'mario_gaming/home.html')

def move_mario(request):
    pass


