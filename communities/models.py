from django.db import models
from core.models import TimeStampedModel


class Community(TimeStampedModel):
    
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    image = models.ImageField()
    views = models.PositiveIntegerField(default=0, verbose_name='조회수')
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="community"
    )  # PROTECT -> 유저가 삭제될 때, 게시물이 삭제되지 않도록 함.

