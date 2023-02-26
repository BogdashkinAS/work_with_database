import csv
from django.core.management.base import BaseCommand
from phones.models import Phone



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding="utf-8") as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        
        for phone in phones:
            Phone.objects.create(id=phone['id'], name=phone['name'], price=phone['price'], image=phone['image'], release_date=phone['release_date'], lte_exists=phone['lte_exists'])
            # TODO: Добавьте сохранение модели
        

