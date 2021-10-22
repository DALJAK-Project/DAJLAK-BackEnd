from rest_framework import serializers

from users.models import User, Bookmark


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "avatar",
            "superhost",)


class ReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "avatar",
            "password",
            "is_superuser",
            "is_staff",
            "date_joined",
            )

class WriteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
    
    def validate_first_name(self, value):
        print(value)
        return value.upper()