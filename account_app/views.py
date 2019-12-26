from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from account_app.forms import SignupForm, LoginForm
from django.contrib import messages


def signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            messages.info(request, f'Successfully created {user.username}')
            return redirect(reverse('accounts:login'))

        messages.error(request, 'Invalid input: Please fix the appropriate fields and try again.')
    else:
        form = SignupForm()

    return render(request, 'account_app/signup.html', {'form': form})

def login_user(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)
                messages.info(request, f'Successfully logged in {user.username}')
                return redirect(reverse('film:index'))
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect(reverse('accounts:login'))
    else:
        form = LoginForm()

    return render(request, 'account_app/login.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    messages.info(request, 'Logged out.')
    return redirect(reverse('accounts:login'))


@login_required
def profile(request):
    return render(request, 'account_app/profile.html')
