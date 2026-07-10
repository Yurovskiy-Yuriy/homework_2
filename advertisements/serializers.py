from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement
from advertisements.models import Advertisement, AdvertisementStatusChoices

class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )
        extra_kwargs = {"status": {"required": False}}

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        request = self.context.get("request")
        user = request.user

        # Проверка на изменение статуса
        if "status" in data:
            current_status = getattr(self.instance, "status", None)
            new_status = data["status"]

            if current_status == AdvertisementStatusChoices.CLOSED and \
                    new_status != AdvertisementStatusChoices.CLOSED:
                raise serializers.ValidationError(
                    "Нельзя открыть закрытое объявление."
                )
        return data