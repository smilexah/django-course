import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Замени 'bookr' на имя твоего проекта
django.setup()  # Загружаем настройки Django

#!/usr/bin/env python3

from reviews.models import Book, Contributor

contributor = Contributor.objects.create(first_names='Packt', last_names='Example Editor', email='PacktEditor@example.com')
book = Book.objects.get(title="Advanced Deep Learning with Keras")
print(book)
book.contributors.add(contributor, through_defaults={'role': 'EDITOR'})