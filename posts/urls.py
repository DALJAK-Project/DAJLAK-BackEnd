from django.urls import path
from . import views
from posts.views import *

urlpatterns = [
    path('post/', views.WritePostList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),
    path('comment/<int:pk>/', CommentDetail.as_view()),
    path('post/<int:post_id>/comment/', CommentList.as_view()),
    # 특정 게시물에 대한 뷰 ('comment/'를 대체함. -> comment 전체 리스트는 필요 x)
    path('user/<int:user_id>/comment/', CommentUserList.as_view()),  # 특정 유저에 대한 뷰
    path('post/search/', views.post_search)
]