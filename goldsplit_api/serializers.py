from rest_framework.serializers import ModelSerializer, CharField, IntegerField
from datetime import datetime

from .models import Runs, Splits, Games
from account.serializers import UserSerializer

class GamesSerializer(ModelSerializer):
    num_runs = IntegerField()

    class Meta:
        model = Games
        fields = ['id', 'name', 'release_year', 'num_runs']

class RunsSerializer(ModelSerializer):
    game_name = CharField(read_only=True, source='game.name')
    user = UserSerializer(read_only=True)

    class Meta:
        model = Runs
        fields = ['id', 'game', 'category_name', 'game_name', 'time', 'upload_date', 'user']

class GamesRunsSerialzier(ModelSerializer):
    #used when details of a specific run are requested, returns all children runs
    #as well as the game info as above
    runs = RunsSerializer(many=True, read_only=True)

    class Meta:
        model = Games
        fields = ['id', 'name', 'release_year', 'runs']

class SplitsSerializer(ModelSerializer):
    class Meta:
        model = Splits
        fields = ['name', 'run', 'time', 'total_time', 'gold_time', 'gold_total_time', 'average_time', 'average_total_time']
