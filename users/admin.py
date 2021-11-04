from django.contrib import admin

from . import models
from django.contrib.auth.admin import UserAdmin


# class BookmarkInline(admin.TabularInline):
#     model = models.Bookmark
#     extra = 1


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {
            "fields": (
                "avatar",
                "favs",
                "favs_community"
            )
        }),
    )   

    list_display = UserAdmin.list_display + ()


# @admin.register(models.Bookmark)
# class BookmarkAdmin(admin.ModelAdmin):
#     list_display = (
#         "user",
#         "post",
#         "active",
#     )
