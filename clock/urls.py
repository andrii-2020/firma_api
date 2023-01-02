from django.urls import path
from .views import RetrieveUpdateDestroyClock, ListCreateClock


urlpatterns = [
    path('listclock', ListCreateClock.as_view()),
    path('clock/<int:pk>', RetrieveUpdateDestroyClock.as_view())
]