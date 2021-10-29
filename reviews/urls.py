from django.urls import path
from . import views
from posts.views import *

urlpatterns = [
    path('review/', views.ReviewList.as_view()),
]