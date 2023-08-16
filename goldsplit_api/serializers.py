from rest_framework import serializers
from .models import Runs, Splits, Games

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['name', 'release_year']

class RunsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Runs
        fields = ['id', 'game', 'category_name']

class SplitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Splits
        fields = ['name', 'run', 'time', 'total_time', 'gold_time', 'gold_total_time', 'average_time']