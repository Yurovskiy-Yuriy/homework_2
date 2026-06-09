import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone_data in phones:
            # Создаем объект Phone из данных CSV
            phone = Phone(
                id=int(phone_data['id']),
                name=phone_data['name'],
                price=int(phone_data['price']),
                image=phone_data['image'],
                release_date=phone_data['release_date'],
                lte_exists=phone_data['lte_exists'].lower() == 'true',
            )
            phone.save()
            self.stdout.write(self.style.SUCCESS(f'Добавлен телефон: {phone.name}'))