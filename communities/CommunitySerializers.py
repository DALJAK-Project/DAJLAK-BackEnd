from posts.models import Post, Comment
from rest_framework import serializers


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
