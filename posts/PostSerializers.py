from posts.models import Post, Comment
from rest_framework import serializers
from django.db import models

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'user', 'desc')


class ReadPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)  # read_only=True

    class Meta:
        model = Post
        fields = ('title', 'category', 'user', 'desc', 'image', 'thumnail_img', 'views', 'comments')

class WritePostSerializer(serializers.Serializer):
    
    title = serializers.CharField(max_length=100)
    desc = serializers.CharField(max_length=300)
    image = serializers.ImageField()
    thumnail_img = serializers.ImageField()
    tag = serializers.CharField(max_length=40)
    views = serializers.IntegerField(default=1)
    category = serializers.CharField(max_length=20)
    
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance, validated_data)

