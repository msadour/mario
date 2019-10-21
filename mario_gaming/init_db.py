from .models import Mario, Princess, Game

if len(Game.objects.all()):
    new_mario = Mario(name="m", position="")
    new_mario.save()
    new_princess = Princess(name="p")
    new_princess.save()
    game_easy = Game(3, new_mario, new_princess)
    game_easy.save()
    game_normal = Game(5, new_mario, new_princess)
    game_normal.save()
    game_hard = Game(10, new_mario, new_princess)
    game_hard.save()
    game_expert = Game(20, new_mario, new_princess)
    game_expert.save()