from django.urls import path 
from .import views

urlpatterns = [
    path('views/', views.book_list),
    path('detail/', views.deatail_view.as_view()),
    ]