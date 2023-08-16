import uuid
from django.db import models

class Games(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    release_year = models.IntegerField()

    def __str__(self):
        return self.name

class Runs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey(Games, on_delete=models.SET_NULL, null=True)
    category_name = models.CharField(max_length=200)

    def __str__(self):
        if self.game is not None:
            return f'{self.game.name} - {self.category_name}'
        else:
            return f'Unknown Game - {self.category_name}'

class Splits(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    time = models.PositiveBigIntegerField()
    total_time = models.PositiveBigIntegerField()
    gold_time = models.PositiveBigIntegerField()
    gold_total_time = models.PositiveBigIntegerField()
    average_time = models.PositiveBigIntegerField()
    run = models.ForeignKey(Runs, on_delete=models.CASCADE)

    def __str__(self):
        return self.name