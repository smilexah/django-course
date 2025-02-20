import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Замени 'bookr' на имя твоего проекта
django.setup()  # Загружаем настройки Django

from reviews.models import Contributor

print(Contributor.objects.all())

Contributor.objects.filter(last_names='Tyrrell').update(first_names='Mike')
print(Contributor.objects.all())

Contributor.objects.get(last_names='Tyrrell').first_names
print(Contributor.objects.get(last_names='Tyrrell').first_names)