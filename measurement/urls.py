from django.urls import path
from .views import SensorListCreateView, SensorRetrieveUpdateView, MeasurementCreateView

urlpatterns = [
    
    #  --- Маршруты для Датчиков (Sensors) ---
    
    # GET /sensors/ - получить список всех датчиков
    # POST /sensors/ - создать новый датчик
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),

    # GET /sensors/<id>/ - получить информацию по конкретному датчику
    # PATCH /sensors/<id>/ - изменить конкретный датчик
    path('sensors/<int:pk>/', SensorRetrieveUpdateView.as_view(), name='sensor-detail-update'),



    # --- Маршрут для Измерений (Measurements) ---
    # POST /measurements/ - добавить новое измерение температуры
    path('measurements/', MeasurementCreateView.as_view(), name='measurement-create'),
    ]