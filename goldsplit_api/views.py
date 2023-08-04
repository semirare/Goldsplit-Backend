from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Runs, Splits
from .serializers import RunsSerializer, SplitsSerializer

class RunsListApiView(APIView):

    def get(self, request, *args, **kwargs):
        runs = Runs.objects.all()
        serializer = RunsSerializer(runs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'game_name': request.data.get('game_name'),
            'category_name': request.data.get('category_name'),
        }
        serializer = RunsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RunDetailsApiView(APIView):

    def get_object(self, run_id):
        try:
            return Runs.objects.get(run_id=run_id)
        except Runs.DoesNotExist:
            return None

    def get(self, request, run_id, *args, **kwargs):

        run_instance = self.get_object(run_id)

        if not run_instance:
            return Response(
                {"res": "Object with run id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = RunsSerializer(run_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, run_id, *args, **kwargs):
        
        run_instance = self.get_object(run_id)

        if not run_instance:
            return Response(
                {"res": "Object with run id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = RunsSerializer(run_instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, run_id, *args, **kwargs):

        run_instance = self.get_object(run_id)

        if not run_instance:
            return Response(
                {"res": "Object with run id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        run_instance.delete()
        return Response(
            {"res": "Run deleted"},
            status=status.HTTP_200_OK
        )