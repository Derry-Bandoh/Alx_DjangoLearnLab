from django.urls import path 
from .views import (
    login_view,
    logout_view,
    register,
    home,
    save,
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView,
    add_comment,
    CommentUpdateView,
    CommentDeleteView,
)


urlpatterns = [
    path('', home, name='home'),
    path('register/', register.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', save, name = 'profile'),
    path('posts/',PostListView.as_view(), name ='post_list' ), 
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'post_detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name ='post_delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post_update'),
    path('post/new/', PostCreateView.as_view(), name = 'post_create'),
    path('posts/<int:post_id>/comments/new/', add_comment, name ='new_comment' ),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name = 'comment_update'),
     path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]