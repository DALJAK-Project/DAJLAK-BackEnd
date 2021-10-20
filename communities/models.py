from django.db import models
from core.models import TimeStampedModel


class Community(TimeStampedModel):
    
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    image = models.ImageField()
    views = models.PositiveIntegerField(default=0, verbose_name='조회수')
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="community"
    )

