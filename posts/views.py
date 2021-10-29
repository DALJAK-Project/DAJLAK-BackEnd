from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter
from posts.PostSerializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.decorators import action

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
        elif self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

@action(detail=False)
def post_search(self, request):

    # 검색 필터 -> 제목 학과 
    title = request.GET.get("title", None)
    # 못찾겠으면 none
    desc = request.GET.get("desc", None)
    tag = request.GET.get("tag", None)
   
    category = request.GET.get("category", None)
    views = request.GET.get("views", None)
    filter_kwargs = {}  
    if views is not None:
        filter_kwargs["views__lt"] = views
    if title is not None:
        filter_kwargs["title__exact"] = title
    if desc is not None:
        filter_kwargs["desc__exact"] = desc
    if tag is not None:
        filter_kwargs["tag__exact"] = tag
    if category is not None:
        filter_kwargs["category__exact"] = category
        
        # o 사용자가 입력한단어가 있을경우
        # filter_kwargs["desc"] = desc
        # filter_kwargs["user"] = user
        # filter_kwargs["tag"] = tag
        # filter_kwargs["category"] = category
    try:
        posts = Post.objects.filter(**filter_kwargs)
    except ValueError:
        posts = Post.objects.all()
    paginator = self.paginator
    results = paginator.paginate_queryset(posts, request)
    serializer = PostSerializer(results, many=True)
    return paginator.get_paginated_response(serializer.data)
        


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


