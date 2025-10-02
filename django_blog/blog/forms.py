from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'bio', 'profile_picture',)

class CustomUserUpdateForm(UserChangeForm):
    
    password = None 

    class Meta:
        model = CustomUser
        
        fields = ('username', 'email', 'bio', 'profile_picture') 
        
        
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }