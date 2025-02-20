import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Замени 'bookr' на имя твоего проекта
django.setup()  # Загружаем настройки Django

from reviews.models import Contributor

contributor = Contributor.objects.get(first_names='Rowel')

contributor.book_set.all()
print(contributor.book_set.all())