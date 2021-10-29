from django.db.models import fields
from reviews.models import Review
from rest_framework import serializers
from django.db import models
from users.UserSerializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ['created']
        read_only_fields = ['id', 'desc', 'user', 'created', 'updated']
        extra_kwargs = {
            'user': {'read_only': True},
        }
      
    def create(self, validated_data):
        return Review.objects.create(**validated_data)

   

    # o this fields read+write