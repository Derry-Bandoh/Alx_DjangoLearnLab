from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,

    )
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import (
    CustomUserCreationForm, 
    CustomUserUpdateForm,
    PostUpdateForm,
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    return render(request, 'blog/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a success page.
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


class register(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by('-published_date')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    form_class = PostUpdateForm
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user 

class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    success_url = reverse_lazy('post-list')
    template_name = 'blog/post_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user 

@login_required
def save(request):
    if request.method == 'POST':
        form  = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid(): 
            form.save()
            return redirect(reverse('profile'))
    else:
        form = CustomUserUpdateForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'blog/profile.html', context)

