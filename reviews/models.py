from django.db import models
from core.models import TimeStampedModel


class Review(TimeStampedModel):
    
    title = models.CharField(max_length=20)
    desc = models.TextField(max_length=30)
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="review"
    )  # PROTECT -> 유저가 삭제될 때, 게시물이 삭제되지 않도록 함.

