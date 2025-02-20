import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Замени 'bookr' на имя твоего проекта
django.setup()  # Загружаем настройки Django

from reviews.models import Contributor

print(Contributor.objects.get(last_names='Wharton'))
Contributor.objects.get(last_names='Wharton').delete()

Contributor.objects.get(last_names='Wharton')