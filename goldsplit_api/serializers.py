from rest_framework import serializers
from .models import Runs, Splits

class RunsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Runs
        fields = ['run_id', 'game_name', 'category_name']

class SplitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Splits
        fields = ['split_name', 'split_time', 'total_time', 'gold_time']