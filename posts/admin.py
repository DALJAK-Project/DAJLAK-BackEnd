from django.contrib import admin
from . import models


class CommentInline(admin.TabularInline):
    model = models.Comment
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (CommentInline, )
    list_display = (
        "id", "title", "category", "user", "views",
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
       "user",
    )

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
     
    )


