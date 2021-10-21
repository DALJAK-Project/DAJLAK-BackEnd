from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter

from posts.PostSerializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # 검색 기능
    filter_backends = [SearchFilter]
    search_fields = ('title', 'desc', )


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



