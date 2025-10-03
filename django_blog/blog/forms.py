from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import (
    CustomUser, 
    Post,
    Comment,
)

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
    
class PostUpdateForm(forms.ModelForm):
    class meta:
        model = Post
        fields = ['title', 'content']

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        
        fields = ['title', 'content'] 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
        }

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 5 : 
            raise forms.ValidationError("Comment must be at least 5 characters long.")
        return content


