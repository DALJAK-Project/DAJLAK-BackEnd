from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {"fields": ()},),
    )

    list_display = UserAdmin.list_display + ()