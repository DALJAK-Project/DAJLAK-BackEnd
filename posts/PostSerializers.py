from django.db.models import fields
from posts.models import Post, Comment
from rest_framework import serializers
from django.db import models
from users.UserSerializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'user', 'desc')


class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, required=False)  # read_only=True

    user = UserSerializer()
    is_bookmark = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Post
        exclude = ('image', )
        read_only_fields = ('id',    )
        
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def get_is_bookmark(self, obj):
        request = self.context.get("request")
        if request:
            user = request.user
            if user.is_authenticated:
                return obj in user.favs.all()
        return False

    # o this fields read+write

    

