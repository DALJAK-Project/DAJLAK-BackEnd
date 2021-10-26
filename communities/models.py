from django.db import models
from core.models import TimeStampedModel


class Community(TimeStampedModel):
    
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    image = models.ImageField(blank=True)
    views = models.PositiveIntegerField(default=0, verbose_name='조회수')
    # like = models.ManyToManyField('users.User', related_name='likes')
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name="community"
    )

    def __str__(self):
        return self.title


class Comment_community(TimeStampedModel):
    community = models.ForeignKey(
        Community, on_delete=models.PROTECT, related_name='comments_community', null=True)
    desc = models.TextField(max_length=300)
    user = models.ForeignKey(
        'users.User', on_delete=models.PROTECT, related_name="comments_users")

    def __str__(self):
        return self.desc

    class Meta:
        db_table = 'comments_community'


class Like(models.Model):
    community = models.ForeignKey('Community', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def count_likes(self):
        return self.user.count()

class Bookmark_community(models.Model):
    community = models.ForeignKey('Community', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)


class Photo(TimeStampedModel):
    file = models.ImageField()
    post = models.ForeignKey(
        "Community", related_name="photos", on_delete=models.CASCADE
    )
    caption = models.CharField(max_length=140)

    def __str__(self):
        return self.community.title
