from django.db import models
from datetime import datetime


class ClockModel(models.Model,):

    clock = models.IntegerField(verbose_name='Відпрацюваних_Годин', default=0, blank=True)
    date_created = models.DateField(auto_now_add=False, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    day = models.CharField(max_length=50, verbose_name='День')

    class Meta:
        db_table = 'clock'

    def __str__(self):
        return self.clock


