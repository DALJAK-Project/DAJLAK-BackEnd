from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): 

    
    # 프로필 
    avatar = models.ImageField(upload_to="avatars", blank=True) 
    superhost = models.BooleanField(default=False)
    #북마크리스트
    # favs = models.ManyToManyField("달작.달작", related_name="favs")



