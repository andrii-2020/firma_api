import json
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ClockModel
from .serializers import Clock_Serialiaer
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ListCreateClock(ListCreateAPIView):
    queryset = ClockModel.objects.all()
    serializer_class = Clock_Serialiaer
    filter_backends = [filters.SearchFilter]
    search_fields = ['clock', 'date_created']

    #http://127.0.0.1:8080/clock/listclock?search=2022-12-03


class RetrieveUpdateDestroyClock(RetrieveUpdateDestroyAPIView):
    queryset = ClockModel.objects.all()
    serializer_class = Clock_Serialiaer

    def post(self, request, *args, **kwargs):
        serializer = Clock_Serialiaer(data=request.data)



