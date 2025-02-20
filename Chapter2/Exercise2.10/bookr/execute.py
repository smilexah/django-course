import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Замени 'bookr' на имя твоего проекта
django.setup()  # Загружаем настройки Django

from reviews.models import Contributor

Contributor.objects.filter(book__title='The Talisman')
print(Contributor.objects.filter(book__title='The Talisman'))