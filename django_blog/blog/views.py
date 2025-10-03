from django.shortcuts import render, redirect, get_object_or_404
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
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from taggit.models import Tag 
from django.db.models import Q
from .forms import (
    CustomUserCreationForm, 
    CustomUserUpdateForm,
    # PostUpdateForm,
    # PostCreateForm,
    PostForm,
    CommentForm,
    )
from .models import Post , Comment


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
    # form_class = PostUpdateForm
    form_class = PostForm
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('post_list')

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

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # form_class = PostCreateForm 
    form_class = PostForm
    
    template_name = 'blog/post_create.html'
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk}) 
    
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

# class CommentCreateView(LoginRequiredMixin, CreateView):
#     model = Comment
#     form_class = 


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'

    def get_success_url(self):
        post_pk = self.object.post.pk
        return reverse('post_detail', kwargs={'pk': post_pk})
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        
        if query:
            search_query = Q(title__icontains=query) | Q(content__icontains=query)
            
            tag_query = Q(tags__name__icontains=query)
            
            queryset = Post.objects.filter(search_query | tag_query).distinct()
        else:
            queryset = Post.objects.none()
            
        return queryset.order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '') 
        return context
    

class TaggedPostListView(ListView):
    model = Post
    template_name = 'blog/tag_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.tag_slug = self.kwargs['tag_slug']
        return Post.objects.filter(tags__slug=self.tag_slug).order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag_slug.replace('-', ' ').title() # Format for display
        return context

class CommentUpdateView(UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_update.html' 

    
    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})




##FUNCTION-BASED VIEWS 
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

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk = pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post 
            comment.author = request.user
            comment.save()
            return redirect(reverse('post_detail', kwargs={'pk': post.pk}))
    return redirect(reverse('post_detail', kwargs={'pk': post.pk}))



