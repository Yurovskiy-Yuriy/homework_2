from django.conf import settings
from django.db import models

from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.db.models import TextChoices



class AdvertisementStatusChoices(models.TextChoices):
    """Статусы объявления."""

    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"


class Advertisement(models.Model):
    """Объявление."""

    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

@receiver(pre_save, sender=Advertisement)
def check_open_ads(sender, instance, **kwargs):
    if not instance.pk: # Проверяем только при создании
        open_count = Advertisement.objects.filter(creator=instance.creator, status=AdvertisementStatusChoices.OPEN).count()
        
        if open_count >= 10:
            raise ValidationError('Превышен лимит открытых объявлений.')
