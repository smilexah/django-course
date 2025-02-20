import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Замени 'bookr' на имя твоего проекта
django.setup()  # Загружаем настройки Django

from reviews.models import Contributor

contributor = Contributor.objects.create(first_names='Rowel', last_names='Atienza', email='RowelAtienza@example.com')
