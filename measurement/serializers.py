from rest_framework import serializers
from .models import Measurement, Sensor

# для создания новых записей о температуре
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']
        read_only_fields = ['created_at']


# для краткого представления датчиков.
class SensorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

# для детального представления одного датчика
class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)
    
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']