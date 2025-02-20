import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Замени 'bookr' на имя твоего проекта
django.setup()  # Загружаем настройки Django

from django.db.models import Q
from reviews.models import Publisher

publishers1 = Publisher.objects.filter(Q(name__startswith="New") | Q(name__startswith="Idea"))
print("Publishers with names starting with 'New' or 'Idea':")
for publisher in publishers1:
    print(publisher.name)

publishers2 = Publisher.objects.filter(Q(name__startswith="New") & Q(name__endswith="Publisher"))
print("\nPublishers with names starting with 'New' and ending with 'Publisher':")
for publisher in publishers2:
    print(publisher.name)