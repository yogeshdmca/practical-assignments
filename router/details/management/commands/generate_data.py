from django.core.management.base import BaseCommand, CommandError
from details.models import Detail
from faker import Faker
from faker.providers import internet
import random


class Command(BaseCommand):
    help = 'Generate dummy data'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        fake = Faker()
        fake.add_provider(internet)

        count = options['count']
        for x in range(count):
            mac_address = "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255))
            Detail.objects.create(sapid=fake.sentence()[:18], hostname=fake.sentence()[:14], loopback=fake.ipv4_private(), mac_address=mac_address)