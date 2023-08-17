from django.contrib.auth.models import User, Group
from django.db import transaction
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import Runs, Splits, Games
from .utils.splitsParser import parseSplits

class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer

class RunsViewSet(viewsets.ModelViewSet):
    queryset = Runs.objects.all()
    serializer_class = RunsSerializer
    
class SplitsViewSet(viewsets.ModelViewSet):
    queryset = Splits.objects.all()
    serializer_class = SplitsSerializer

class SplitsUploadView(APIView):

    @transaction.atomic
    def post(self, request):
        splits_file = request.data['splits_file']
        splits = parseSplits(splits_file)

        game = Games.objects.create_game(name=splits['game_name'])
        run = Runs.objects.create_run(game=game, category=splits['category'])
        for split in splits['splits']:
            Splits.objects.create_split(
                                        run=run,
                                        name=split['name'],
                                        time=split['time'],
                                        total_time=split['total_time'],
                                        gold_time=split['gold_time'],
                                        gold_total_time=split['gold_total_time'],
                                        average_time=split['average_time']
            )

        return Response(status=200)