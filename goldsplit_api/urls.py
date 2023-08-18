from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('runs', RunsViewSet)
router.register('splits', SplitsViewSet)
router.register('games', GamesViewSet)
#router.register('upload', SplitsUploadView, basename="upload")

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', SplitsUploadView.as_view()),
    path('run/details/<str:run_id>/', RunDetailsView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]