from django.db import models
from core.models import TimeStampedModel


class Comment(TimeStampedModel):

    desc = models.TextField(max_length=300)
    image = models.ImageField()
    # user = models.ForeignKey(
    #     "users.User", on_delete=models.CASCADE, related_name="users"
    # )


