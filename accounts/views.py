from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm


# Create your views here.
# 회원가입
def signup(request):
    if request.user.is_authenticated:
        return redirect('maps:main')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('maps:main')
    else:
        form = CustomUserCreationForm()
    context = {
        'signup_form': form,
    }
    return render(request, 'accounts/signUp.html', context)

# 로그인
def login(request):
    if request.user.is_authenticated:
        return redirect('maps:main')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'maps:main')
    else:
        form = AuthenticationForm()
    context = {
        'login_form' : form, 
    }
    return render(request, 'accounts/signUp.html', context)

# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('maps:main')

def mypage(request, username):
    myinfo = get_object_or_404(get_user_model(), username=username)
    context = {'myinfo': myinfo, }
    return render(request, 'accounts/mypage.html', context)