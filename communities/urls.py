from django.urls import path
from .views import *

urlpatterns = [
    path('community/', CommunityListAPIView.as_view()),
    path('community/<int:pk>/', CommunityDetailAPIView.as_view()),
]
