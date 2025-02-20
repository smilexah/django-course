import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')  # Replace 'bookr' with your project name
django.setup()  # Load Django settings

from django.db.models import Q
from reviews.models import Publisher

publishers = Publisher.objects.filter(Q(name__startswith="New") | Q(name__endswith="Publisher"))
print("Filtered Publishers:")
for publisher in publishers:
    print(publisher.name)

try:
    new_town_publisher = Publisher.objects.get(name='New Town Publisher')
    print(f"\nIs 'New Town Publisher' in the queryset? {'Yes' if new_town_publisher in publishers else 'No'}")
except Publisher.DoesNotExist:
    print("\n'New Town Publisher' does not exist in the database.")

try:
    byron_bay_press = Publisher.objects.get(name='Byron Bay Press')
    print(f"Is 'Byron Bay Press' in the queryset? {'Yes' if byron_bay_press in publishers else 'No'}")
except Publisher.DoesNotExist:
    print("'Byron Bay Press' does not exist in the database.")


publishers = Publisher.objects.filter(Q(name__startswith="New") | Q(name__endswith="Publisher"))

new_town_publisher = Publisher.objects.get(name='New Town Publisher')

publishers.contains(new_town_publisher)

publishers.contains(Publisher.objects.get(name='Byron Bay Press'))
