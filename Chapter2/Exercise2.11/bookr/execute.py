import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Замени 'bookr' на имя твоего проекта
django.setup()  # Загружаем настройки Django

from reviews.models import Book

book = Book.objects.get(title='The Talisman')
print(book)

book.contributors.all()
print(book.contributors.all())