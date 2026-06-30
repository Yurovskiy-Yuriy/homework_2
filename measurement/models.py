from django.db import models

# https://github.com/netology-code/dj-homeworks/tree/video/3.1-drf-intro/smart_home

# модель датчика
class Sensor(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя датчика')
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name

# модель измерения
class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        verbose_name="Датчик",
        related_name='measurements',
        default=1,
    )
    temperature = models.FloatField(verbose_name="Температура")
    created_at = models.DateTimeField(
        verbose_name = "Дата и время измерения",
        auto_now_add = True  # Автоматически устанавливает время при создании записи
    )

    class Meta:
        # Измерения будут по умолчанию сортироваться по убыванию даты
        ordering = ['-created_at'] 

    def __str__(self):
        return f"Измерение от {self.created_at} для {self.sensor.name}"
    
