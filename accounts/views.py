from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile, NotificationsModel
from .forms import UserSignUpModelForm, UserProfileSignUpModelForm, LoginForm
from .libs import RandomDigitsGen
from django.contrib.auth import logout, login, authenticate
from django.http import JsonResponse
# Create your views here.

def Signup(request):
    user_form = UserSignUpModelForm()
    userprofile_form = UserProfileSignUpModelForm()

    if request.method == 'POST':
        user_form = UserSignUpModelForm(data=request.POST)
        userprofile_form = UserProfileSignUpModelForm(data=request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():
            password = user_form.cleaned_data.get('password')

            user = user_form.save(commit=False)
            user.username = RandomDigitsGen()
            user.set_password(password)

            userprofile = userprofile_form.save(commit=False)
            userprofile.user = user

            user.save()
            userprofile.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('Login')
        else:messages.error(request, user_form.errors+userprofile_form.errors)
    return render(request, 'accounts/signup.html', {'user_form':user_form, "userprofile_form":userprofile_form})

def Login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            users = User.objects.filter(email=email)
            if users.exists():
                user = users.first()
                user = authenticate(username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Success')
                    return redirect('DashboardHome')
                else:messages.error(request, 'wrong email or password')
            else:messages.error(request, 'user dos not exists')
        else:messages.error(request, form.errors)
    return render(request, 'accounts/login.html', {'form':form})

def Logout(request):
    logout(request)
    return redirect('Login')


