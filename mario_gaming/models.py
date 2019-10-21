from django.db import models

class Solution(models.Model):
    niveau = models.IntegerField(default=3)

    def __init__(self, *args, **kwargs):
        super(Solution, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)

class Combinaison(models.Model):
    name = models.CharField(max_length=100, default="")
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, null=True, related_name='combinaisons')

    def __init__(self, *args, **kwargs):
        super(Combinaison, self).__init__(*args, **kwargs)
        self.__dict__.update(kwargs)


