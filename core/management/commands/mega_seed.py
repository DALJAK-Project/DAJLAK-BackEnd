import random
from datetime import datetime
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from posts.models import Post, Comment, Photo



class Command(BaseCommand):

    help = "It seeds the DB with tons of stuff"

    def handle(self, *args, **options):
        user_seeder = Seed.seeder()
        user_seeder.add_entity(User, 20, {"is_staff": False, "is_superuser": False})
        user_seeder.execute()

        users = User.objects.all()
        posts = Post.objects.all()
        post_seeder = Seed.seeder()
        post_seeder.add_entity(
            Post,
            150,
            {
               "title": lambda x: post_seeder.faker.text(),
               "desc": lambda x: post_seeder.faker.text(),
               "tag": lambda x: post_seeder.faker.words(),
               "views": lambda x: random.randint(0, 30),
               "user" : lambda x: random.choice(users),

           },
      
        )
        post_seeder.add_entity(
            Comment,
           30, 
           {
               'post': lambda x: random.choice(posts),
               'desc': lambda x: post_seeder.faker.text(),
               'user': lambda x: random.choice(users),
           }
        )
        post_seeder.execute()


        for post in posts:
            for i in range(random.randint(5, 15)):
                Photo.objects.create(
                    caption=post_seeder.faker.text(),
                    post=post,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )
     


        # o comment도 추추가 

        self.stdout.write(self.style.SUCCESS(f"Everything seeded"))
