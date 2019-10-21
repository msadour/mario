from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('game', views.game_page, name="game"),
    path('move_mario', views.move_mario, name="move_mario"),
    path('solutions', views.solutions, name="solutions")
]
