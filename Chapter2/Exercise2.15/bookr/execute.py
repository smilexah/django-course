import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Замени 'bookr' на имя твоего проекта
django.setup()  # Загружаем настройки Django

from reviews.models import Publisher

Publisher.objects.bulk_create([
    Publisher(name="New Town Publisher", website="www.newtownexample.com", email='newtow@email.com'),
    Publisher(name="Byron Bay Press", website="www.byronbayexample.com", email='byronbayexample@email.com'),
    Publisher(name="Katoomba Publisher", website="www.katoombaexample.com", email='katoombaexample@email.com')]
)

print(Publisher.objects.all())