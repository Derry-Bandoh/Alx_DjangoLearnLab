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
)


urlpatterns = [
    path('', home, name='home'),
    path('register/', register.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', save, name = 'profile'),
    path('posts/',PostListView.as_view(), name ='post-list' ), 
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'post-detail'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name ='post-delete'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name = 'post-update'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
]