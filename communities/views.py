from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from communities.CommunitySerializers import CommunitySerializer
from communities.models import Community


class CommunityListAPIView(APIView):
    def get(self, request):
        communities = Community.objects.all()
        serializer = CommunitySerializer(communities, many=True)
        return Response(serializer.data)

    def post(self, request):  # 로그인 상태에서만 커뮤니티 작성 가능
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommunityDetailAPIView(APIView):
    def get_object(self, pk):  # 존재하는 인스턴스인지 판단하고, 존재한다면 그것을 리턴함.
        return get_object_or_404(Community, pk=pk)

    def get(self, request, pk):
        community = self.get_object(pk)
        serializer = CommunitySerializer(community)
        return Response(serializer.data)

    def put(self, request, pk):
        community = self.get_object(pk)
        if community.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = CommunitySerializer(community, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        community = self.get_object(pk)
        if community.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



