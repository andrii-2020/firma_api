from rest_framework.serializers import ModelSerializer
from datetime import datetime
from .models import ClockModel
import datetime


class Clock_Serialiaer(ModelSerializer):

    class Meta:
         model = ClockModel
         fields = ('__all__')

