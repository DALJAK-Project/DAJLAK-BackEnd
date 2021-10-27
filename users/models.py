from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    # 프로필 
    avatar = models.ImageField(upload_to="avatars", blank=True) 
    superhost = models.BooleanField(default=False)
    favs = models.ManyToManyField("posts.Post", related_name="favs", blank=True)
    favs_community = models.ManyToManyField("communities.Community", related_name="favs_community", blank=True)
