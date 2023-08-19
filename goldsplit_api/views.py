from django.contrib.auth.models import User, Group
from django.db import transaction
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, ValidationError

from .serializers import *
from .models import Runs, Splits, Games
from .utils.splitsParser import parseSplits

class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer

class RunsViewSet(viewsets.ModelViewSet):
    queryset = Runs.objects.all()
    serializer_class = RunsSerializer      

class RunDetailsView(APIView):

    def get(self, request, run_id):
        if not run_id:
            raise ParseError()
        
        try:
            run = Runs.objects.get(id=run_id)
        except:
            raise ValidationError

        splits = run.splits_set.all().order_by('total_time')

        split_serializer = SplitsSerializer(splits, many=True)
        
        run_data = {
            'game_name': run.game.name,
            'category_name': run.category_name,
            'total_time': splits[len(splits)-1].total_time,
            'splits': split_serializer.data
        }

        return Response(data=run_data, status=200)
    
class SplitsViewSet(viewsets.ModelViewSet):
    queryset = Splits.objects.all()
    serializer_class = SplitsSerializer

class SplitsUploadView(APIView):

    @transaction.atomic
    def post(self, request):
        splits_file = request.data['splits_file']
        splits = parseSplits(splits_file)

        #check if games is already in db, if not then create it
        game = Games.objects.filter(name=splits['game_name'])
        if game.exists():
            game = game[0]
        else:        
            game = Games.objects.create_game(name=splits['game_name'])   

        run = Runs.objects.create_run(game=game, category=splits['category'], time=splits['time'])
        for split in splits['splits']:
            Splits.objects.create_split(
                                        run=run,
                                        name=split['name'],
                                        time=split['time'],
                                        total_time=split['total_time'],
                                        gold_time=split['gold_time'],
                                        gold_total_time=split['gold_total_time'],
                                        average_time=split['average_time'],
                                        average_total_time=split['average_total_time']
            )
        data = {'run_id': run.id}

        return Response(data=data, status=200)