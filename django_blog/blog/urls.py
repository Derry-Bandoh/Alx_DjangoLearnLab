from django.urls import path 
from .views import (
    login_view,
    logout_view,
    SignUpView,
    home,

)


urlpatterns = [
    path('', home, name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name = 'profile')
    
]