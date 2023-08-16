from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RunsSerializer, SplitsSerializer, GamesSerializer
from .models import Runs, Splits, Games

class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer

class RunsViewSet(viewsets.ModelViewSet):
    queryset = Runs.objects.all()
    serializer_class = RunsSerializer
    
class SplitsViewSet(viewsets.ModelViewSet):
    queryset = Splits.objects.all()
    serializer_class = SplitsSerializer