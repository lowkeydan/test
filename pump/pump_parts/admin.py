from django.contrib import admin
from . models import Pump_type
# Register your models here.
@admin.register(Pump_type)
class Pump_type_Admin(admin.ModelAdmin):
    fields = (('pump_type', 'pump_price'),)



#admin.site.register(Pump_type)