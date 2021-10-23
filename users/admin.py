from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin


# class BookmarkInline(admin.TabularInline):
#     model = models.Bookmark
#     extra = 1


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    # inlines = (BookmarkInline, )
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {
            "fields": (
                "avatar",
                "favs",
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
