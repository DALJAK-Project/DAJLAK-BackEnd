from django.contrib import admin
from . import models


class CommentCommunityInline(admin.TabularInline):
    model = models.Comment_community
    extra = 1


@admin.register(models.Community)
class CommunityAdmin(admin.ModelAdmin):
    inlines = (CommentCommunityInline, )
    list_display = (
        "title", "user", "views",
    )


@admin.register(models.Comment_community)
class CommentCommunityAdmin(admin.ModelAdmin):
    list_display = (
        "user", "desc",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (

    )