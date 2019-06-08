from django.db import models

# Create your models here.
class Pump_type(models.Model):
    pump_type = models.CharField(max_length=20, verbose_name='水泵型号')
    pump_price = models.IntegerField(default=0)