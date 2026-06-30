from django.contrib import admin
from .models import Sensor, Measurement

"""для модели Sensor"""
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name', 'description']


"""для модели Measurement"""
@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):

    list_display = ('sensor', 'temperature', 'created_at')
    list_filter = ('sensor__name',)
    date_hierarchy = 'created_at'
    search_fields = ['temperature', 'sensor__name']