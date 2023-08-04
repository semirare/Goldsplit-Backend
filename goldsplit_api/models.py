import uuid
from django.db import models

# Create your models here.
class Runs(models.Model):
    run_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game_name = models.CharField(max_length=200)
    category_name = models.CharField(max_length=200)

    def __str__():
        return f'{game_name} - {category_name}'

class Splits(models.Model):
    split_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    split_name = models.CharField(max_length=200)
    split_time = models.TimeField()
    total_time = models.TimeField()
    gold_time = models.TimeField()
    run = models.ForeignKey(Runs, on_delete=models.CASCADE)

    def __str__():
        return split_name