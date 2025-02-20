import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Замени 'bookr' на имя твоего проекта
django.setup()  # Загружаем настройки Django

from reviews.models import Book, BookContributor, Contributor

contributor = Contributor.objects.get(first_names='Rowel')
print(contributor)
book = Book.objects.get(title='Advanced Deep Learning with Keras')
print(book)
book_contributor = BookContributor(book=book, contributor=contributor, role='AUTHOR')
book_contributor.save()