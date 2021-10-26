from django.db import models
from core.models import TimeStampedModel

category_select = (
    ('교과대학', '교과대학'),
    ('인문대학', '인문대학'),
    ('경영대학', '경영대학'),
    ('경영대학', '경영대학'),
    ('농식품융합대학', '농식품융합대학'),
    ('약학대학', '약학대학'),
    ('사범대학', '사범대학'),
    ('자연과학대학', '자연과학대학'),
    ('한의과대학', '한의과대학'),
    ('조형예술디자인대학', '조형예술디자인대학'),
    ('창의공과대학', '창의공과대학'),
    ('치과대학', '치과대학'),
    ('의과대학', '의과대학'),
)


class Post(TimeStampedModel):

    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    image = models.ImageField(blank=True)
    thumnail_img = models.ImageField()
    tag = models.CharField(max_length=40)
    views = models.PositiveIntegerField(default=0, verbose_name='조회수')
    category = models.CharField(max_length=20, choices=category_select, default='일반')
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts"
    )
    # comments = models.ForeignKey(
    #     "comments.Comment", on_delete=models.CASCADE, related_name="poco"
    # )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments', null=True)
    desc = models.TextField(max_length=300)
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="users"
    )

    def __str__(self):
        return self.desc

    class Meta:
        db_table = 'comments'


class Photo(TimeStampedModel):

    file = models.ImageField()
    post = models.ForeignKey(
        "posts.Post", related_name="photos", on_delete=models.CASCADE
    )
    caption = models.CharField(max_length=140)

    def __str__(self):
        return self.room.name


# o 여기서 해야할것은?

# o 카테고리 

# class AbstractItem(TimeStampedModel):
#     """ Abstract Item """
#
#     name = models.CharField(max_length=40)
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return self.name


# class Category(models.Model):
#     name = models.CharField(max_length=20)
#
#     class Meta:
#         abstract = True
