from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from posts.PostSerializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination


class OwnPagination(PageNumberPagination):
    page_size = 20


# o post기능에 좀더 디테일을 추가하기 위해서
# o Rooms
class WritePostList(APIView): 
    def get(self, request):
        paginator = OwnPagination()
        posts = Post.objects.all()
        results = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(results, many=True, context={"request": request})
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save(user=request.user)
            post_serializer = PostSerializer(post).data
            return Response(data=post_serializer, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # 검색 기능
    filter_backends = [SearchFilter]
    search_fields = ('title', 'desc', )


class PostDetail(APIView):
    def get_post(self, pk):
        try:
            post = Post.objects.get(pk=pk)
            return post
        except Post.DoesNotExist:
            return None

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        if post is not None:
            serializer = PostSerializer(post).data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        if post is not None:
            if post.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                post = serializer.save()
                return Response(PostSerializer(post).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        if post is not None:
            if post.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            post.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CommentList(APIView):
    def get(self, request, post_id, *args, **kwargs):
        comments = Comment.objects.filter(post=post_id)
        serializer_class = CommentSerializer(comments, many=True).data
        return Response(serializer_class)

    def post(self, request, post_id):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentUserList(APIView):
    def get(self, request, user_id, *args, **kwargs):
        comments = Comment.objects.filter(user=user_id)
        serializer_class = CommentSerializer(comments, many=True).data
        return Response(serializer_class)


class CommentDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Comment, pk=pk)

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        if comment.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        if comment.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def post_search(request):

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

    paginator = OwnPagination()
    
    results = paginator.paginate_queryset(posts, request)
    serializer = PostSerializer(results, many=True)
    return paginator.get_paginated_response(serializer.data)