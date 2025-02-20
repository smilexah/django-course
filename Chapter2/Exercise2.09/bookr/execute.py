import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Замени 'bookr' на имя твоего проекта
django.setup()  # Загружаем настройки Django

from reviews.models import Contributor

Contributor.objects.create(first_names='Peter', last_names='Wharton', email='PeterWharton@example.com')
Contributor.objects.create(first_names='Peter', last_names='Tyrrell', email='PeterTyrrell@example.com')
contributors = Contributor.objects.filter(first_names='Peter')
print(contributors)
Contributor.objects.filter(first_names='Rowel')
print(Contributor.objects.filter(first_names='Rowel'))
Contributor.objects.filter(first_names='Nobody')
print(Contributor.objects.filter(first_names='Nobody'))