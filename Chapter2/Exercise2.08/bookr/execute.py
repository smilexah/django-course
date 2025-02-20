import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Замени 'bookr' на имя твоего проекта
django.setup()  # Загружаем настройки Django

from reviews.models import Contributor

contributors = Contributor.objects.all()

print(contributors)
print(contributors[0])
print(contributors[0].first_names)
print(contributors[0].last_names)