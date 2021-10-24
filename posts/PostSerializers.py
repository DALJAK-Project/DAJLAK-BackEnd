from posts.models import Post, Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'user', 'desc')


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)  # read_only=True

    class Meta:
        model = Post
        fields = ('title', 'category', 'user', 'desc', 'image', 'thumnail_img', 'views', 'comments')


