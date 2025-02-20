import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Замени 'bookr' на имя твоего проекта
django.setup()  # Загружаем настройки Django

from reviews.models import Publisher

publisher = Publisher.objects.get(name='Pocket Books')
print(publisher)
print(publisher.name)
print(publisher.website)
print(Publisher.objects.get(id=1))