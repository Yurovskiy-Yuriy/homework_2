from rest_framework import generics
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer

# --- Обработчики для Датчиков (Sensor) ---

class SensorListCreateView(generics.ListCreateAPIView):
    """
    GET /sensors/ - Получить список всех датчиков.
    POST /sensors/ - Создать новый датчик.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    GET /sensors/<id>/ - Получить детальную информацию о конкретном датчике.
    PATCH /sensors/<id>/ - Частично обновить информацию о датчике.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# --- Обработчики для Измерений (Measurement) ---
class MeasurementCreateView(generics.CreateAPIView):
    """
    POST /measurements/ - Добавить новое измерение температуры.
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer