from django_seed import Seed
from django.core.management.base import BaseCommand

import communities
from users.models import User
from communities.models import Community, Comment_community
import random


class Command(BaseCommand):

    help = "This command good"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=100, type=int, help="How many seed?")

    def handle(self, *args, **options):

        number = options.get("number")
        seeder = Seed.seeder()
        users = User.objects.all()
        communities = Community.objects.all()
        seeder.add_entity(Community, number, {
            "title": lambda x: seeder.faker.text(),
            "desc": lambda x: seeder.faker.text(),
            "views": lambda x: random.randint(0, 30),
            "user": lambda x: random.choice(users),
        })

        seeder.add_entity(
            Comment_community,
            30,
            {
                'community': lambda x: random.choice(communities),
                'desc': lambda x: seeder.faker.text(),
                'user': lambda x: random.choice(users),
            }
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f'{number} users created!'))