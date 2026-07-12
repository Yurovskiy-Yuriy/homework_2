from django_filters import rest_framework as filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # фильтр по статусу
    status = filters.ChoiceFilter(
        field_name='status',
        choices=[
        (AdvertisementStatusChoices.OPEN, "Открыто"),
        (AdvertisementStatusChoices.CLOSED, "Закрыто")
    ])
    
    # фильтр по дате
    created_at = filters.DateTimeFromToRangeFilter(
        label="Дата создания (диапазон)",
        help_text="Формат: YYYY-MM-DDTHH:MM:SSZ или YYYY-MM-DD. Пример: ?created_at_after=2026-07-01&created_at_before=2026-07-05"
    )

    class Meta:
        model = Advertisement
        
        fields = ['created_at', 'status']