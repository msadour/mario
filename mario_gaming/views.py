import json
from itertools import product

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

from .classes import Mario, Princess, Game
from .models import Solution, Combinaison

mario = Mario(name="m", position=(0,2))
princess = Princess(name="p")
game = Game(3, mario, princess)
data = {'mario': mario, 'princess': princess, 'game': game}


def home(request):
    return render(request, 'mario_gaming/home.html')

def game_page(request):
    game.win = False
    mario.position = (0,2)
    data['possibilities'] = game.get_possibilities()
    return render(request, 'mario_gaming/game.html', data)

def move_mario(request):
    direction = request.GET.get('direction', None)
    if direction in game.get_possibilities():
        game.move_mario(mario, direction)
        win = game.win
        game_updated = render_to_string('mario_gaming/table_game.html', {'game': game})
        new_possibilities = render_to_string('mario_gaming/table_buttons.html', {'possibilities': game.get_possibilities()})
        return HttpResponse(json.dumps({'game_updated': game_updated, 'new_possibilities': new_possibilities, 'win': win}))

def solutions(request):
    if len(Solution.objects.all()) == 0:
        solution = Solution(niveau=3)
        solution.save()
        directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        # 'possibilities' allow us all combinaisation of all direction (all combinaison
        # contain three directions) to test if each one allow Mario to save the princess
        combinaisons = [possibility for possibility in product(directions, repeat=3)]

        for combinaison in combinaisons:
            mario = Mario('m', (0, 2))
            princess = Princess('p')
            game = Game(3, mario, princess)
            for direction in combinaison:
                if direction in game.get_possibilities():
                    game.move_mario(mario, direction)
                if game.win:
                    new_combinaison = Combinaison(name=str(combinaison).replace('\'',''), solution=solution)
                    new_combinaison.save()

    data['solution'] = Solution.objects.filter(niveau=3).first()
    return render(request, 'mario_gaming/solution.html', data)


