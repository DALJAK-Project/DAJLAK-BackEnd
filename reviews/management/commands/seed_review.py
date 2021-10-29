from django_seed import Seed
from django.core.management.base import BaseCommand
from users.models import User
from reviews.models import Review
import random

class Command(BaseCommand):

    help = "This command good"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=1, type=int, help="How many seed?")

    def handle(self, *args, **options):

        number = options.get("number")
        seeder = Seed.seeder()
        users = User.objects.all()
        seeder.add_entity(Review, number, {
            "title": lambda x: seeder.faker.text(),
            "desc": lambda x: seeder.faker.text(),
            "user": lambda x: random.choice(users),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} users created!'))