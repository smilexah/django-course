import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Замени 'bookr' на имя твоего проекта
django.setup()  # Загружаем настройки Django

from reviews.models import Publisher

publishers = [Publisher.objects.get(name='New Town Publisher'), Publisher.objects.get(name='Byron Bay Press')]
print(publishers)

publishers[0].website = "www.newsouthwalespublisher.com"
print(publishers[0].website)
publishers[1].website = "www.newsouthwalespublisher.com"
print(publishers[1].website)

Publisher.objects.bulk_update(publishers, ["website"])
for publisher in Publisher.objects.all():
    print(publisher.website)