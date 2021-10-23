from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    # 프로필 
    avatar = models.ImageField(upload_to="avatars", blank=True) 
    superhost = models.BooleanField(default=False)
    favs = models.ManyToManyField("posts.Post", related_name="favs")
    bio = models.TextField(max_length=300)


# class Bookmark(models.Model):
#     user = models.ForeignKey('User', on_delete=models.CASCADE)
#     post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
#     active = models.BooleanField(default=False)

#     class Meta:
#         db_table = "bookmark"



# o 뭐해야하지?? 일단 코멘트를 post로 옮겼고 북마크 기능도 옮겨야해
# o 지금은? user에 fav를 생성하는 이유눈? 클릭하면 fav데이터를 받아야하니깐