from django.urls import path, include
from .views import (
    RunsListApiView,
    RunDetailsApiView
)

urlpatterns = [
    path('runs', RunsListApiView.as_view()),
    path('runs/<str:run_id>', RunDetailsApiView.as_view())
]