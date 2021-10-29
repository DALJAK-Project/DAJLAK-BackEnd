from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from reviews.ReviewSerializers import ReviewSerializer
from .models import Review
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class OwnPagination(PageNumberPagination):
    page_size = 20


# Create your views here
class ReviewList(APIView): 
     
    def get(self, request):
        paginator = OwnPagination()
        reviews = Review.objects.all()
        results = paginator.paginate_queryset(reviews, request)
        serializer = ReviewSerializer(results, many=True, context={"request": request})
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save(user=request.user)
            post_serializer = ReviewSerializer(post).data
            return Response(data=post_serializer, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



   