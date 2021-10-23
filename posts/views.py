from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from posts.PostSerializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment
from rest_framework import status
from rest_framework.views import APIView
from users.UserSerializers import ReadSerializer

# o post기능에 좀더 디테일을 추가하기 위해서
# o Rooms
class WritePostList(APIView): 
    def get(self, request):
        posts = Post.objects.all()
        serializer_class = PostSerializer(posts, many=True).data
        return Response(serializer_class)

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









class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



