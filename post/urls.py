from django.urls import path
from .views import (
    RegisterView, LoginView, PostListView,
    PostCreateView, PostDetailView, CommentCreateView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
]
