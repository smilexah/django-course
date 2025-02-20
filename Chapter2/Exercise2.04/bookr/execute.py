import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Замени 'bookr' на имя твоего проекта
django.setup()  # Загружаем настройки Django

from datetime import date
from reviews.models import Book, Publisher

publisher = Publisher.objects.get(name='Packt Publishing')

print(publisher)

book = Book.objects.create(title='Advanced Deep Learning with Keras', publication_date=date(2018, 10, 31),
                           isbn='9781788629416', publisher=publisher)