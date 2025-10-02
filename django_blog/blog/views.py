from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm , CustomUserUpdateForm



def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a success page.
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

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
    return render(request, 'profile.html', context)

