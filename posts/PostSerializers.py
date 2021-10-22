from django.db.models import fields
from posts.models import Post, Comment
from rest_framework import serializers
from django.db import models
from users.UserSerializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'user', 'desc')


class ReadPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)  # read_only=True
    user = UserSerializer()
    class Meta:
        model = Post
        fields = ('title', 'category', 'user', 'desc', 'image', 'thumnail_img', 'views', 'comments')

class WritePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
    
    
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance, validated_data)

