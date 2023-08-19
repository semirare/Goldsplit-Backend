from rest_framework.serializers import ModelSerializer, CharField
from .models import Runs, Splits, Games

class GamesSerializer(ModelSerializer):
    class Meta:
        model = Games
        fields = ['name', 'release_year']

class RunsSerializer(ModelSerializer):
    game_name = CharField(read_only=True, source='game.name')

    class Meta:
        model = Runs
        fields = ['id', 'game', 'category_name', 'game_name', 'time']

class SplitsSerializer(ModelSerializer):
    class Meta:
        model = Splits
        fields = ['name', 'run', 'time', 'total_time', 'gold_time', 'gold_total_time', 'average_time', 'average_total_time']
