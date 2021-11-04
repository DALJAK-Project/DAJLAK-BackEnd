from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from communities.CommunitySerializers import CommunitySerializer
from communities.models import Community
from posts.models import Post
from .models import User
from users.UserSerializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from posts.PostSerializers import PostSerializer
from posts.models import Post
import jwt 
# json web tokken
from django.conf import settings
from django.contrib.auth import authenticate


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(UserSerializer(new_user).data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class MeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(["GET"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        return Response(UserSerializer(user).data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


class BookmarksView(APIView):

    permission_classes = [IsAuthenticated]  # 특정 유저일때

    def get(self, request):
        user = request.user
        serializer = PostSerializer(user.favs.all(), many=True).data
        return Response(serializer)

    def put(self, request):
        # o 우선 pk를 가져오고
       pk = request.data.get("pk", None)
       user = request.user
       if pk is not None:
           try:
               post = Post.objects.get(pk=pk)
               if post in user.favs.all():
                   user.favs.remove(post)
               else:
                   user.favs.add(post)
               return Response()
           except Post.DoesNotExist:
               pass
       return Response(status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request):


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if not username or not password:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    # o 토큰을 받아서 그 토큰으로 user찾고 그 유저를 리턴
    if user is not None:
        encoded_jwt = jwt.encode(
            {"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256"
        )
        return Response(data={"token": encoded_jwt})
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

