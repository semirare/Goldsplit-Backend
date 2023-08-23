import uuid
from datetime import datetime
from django.db import models
from django.conf import settings

class GamesManager(models.Manager):
    def create_game(self, name):
        game = self.create(name=name)

        return game

class Games(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)
    release_year = models.IntegerField(null=True)

    objects = GamesManager()

    def __str__(self):
        return self.name

class RunsManager(models.Manager):
    def create_run(self, game, category, time, user):
        run = self.create(game=game, category_name=category, time=time, user=user)

        return run

class Runs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey(Games, on_delete=models.SET_NULL, null=True)
    category_name = models.CharField(max_length=200)
    time = models.PositiveBigIntegerField()
    upload_date = models.DateTimeField(editable=False, default=datetime.now())
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )

    objects = RunsManager()

    def __str__(self):
        if self.game is not None:
            return f'{self.game.name} - {self.category_name}'
        else:
            return f'Unknown Game - {self.category_name}'

class SplitsManager(models.Manager):
    def create_split(self, run, name, time, total_time, gold_time, gold_total_time, average_time, average_total_time):
        split = self.create(
                        run=run,
                        name=name,
                        time=time,
                        total_time=total_time,
                        gold_time=gold_time,
                        gold_total_time=gold_total_time,
                        average_time=average_time,
                        average_total_time=average_total_time
        )

        return split

class Splits(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    time = models.PositiveBigIntegerField()
    total_time = models.PositiveBigIntegerField()
    gold_time = models.PositiveBigIntegerField()
    gold_total_time = models.PositiveBigIntegerField()
    average_time = models.PositiveBigIntegerField()
    average_total_time = models.PositiveBigIntegerField()
    run = models.ForeignKey(Runs, on_delete=models.CASCADE)

    objects = SplitsManager()

    def __str__(self):
        return self.name
    