from django.urls import path
from . import views
from posts.views import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register("", views.PostViewSet)

# urlpatterns = [
#     path('post/', views.WritePostList.as_view()),
#     path('post/<int:pk>/', PostDetail.as_view()),
#     path('comment/', CommentList.as_view()),
#     path('comment/<int:pk>', CommentDetail.as_view()),
#     path('post/search/', views.post_search)
# ]

urlpatterns = router.urls