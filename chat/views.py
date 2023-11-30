from django.shortcuts import render, redirect

from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate, login

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('chat-page')  # Change 'dashboard' to the appropriate URL name
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'chat/loginpage.html')  # Update with your template path

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('chat-page')
    else:
        form = SignUpForm()
    
    return render(request, 'chat/signuppage.html', {'form': form})
