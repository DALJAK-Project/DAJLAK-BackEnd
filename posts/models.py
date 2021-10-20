from django.db import models
from core.models import TimeStampedModel
from core.models import TimeStampedModel

class Post(TimeStampedModel):

    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    image = models.ImageField()
    thumnail_img = models.ImageField()
    tag = models.CharField(max_length=40)
    views = models.PositiveIntegerField(default=0, verbose_name='조회수')
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts"
    )
    # comments = models.ForeignKey(
    #     "comments.Comment", on_delete=models.CASCADE, related_name="poco"
    # )

    def __str__(self):
        return self.name



class Comment(TimeStampedModel):

    desc = models.TextField(max_length=300)
    image = models.ImageField()
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="users"
    )

# o 여기서 해야할것은?

# o 카테고리 

class AbstractItem(TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=40)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(TimeStampedModel):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True 

  
