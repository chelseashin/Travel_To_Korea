from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import MyUser
from .forms import CustomUserCreationForm

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, SearchUserSerializer

# python manage.py makemigrations accounts

# Create your views here.
# 회원가입
def signup(request):
    if request.user.is_authenticated:
        return redirect('maps:main')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)    # 폼 처리
            user_form.username = user_form.nickname
            user_form.nickname = user_form.nickname
            user_form.email = user_form.email
            user_form.gender = user_form.gender
            user_form.birth = user_form.birth
            print(user_form)
            # user_form.username = MyUser.nickname
            user = user_form.save()
            print(user.nickname)
            # user = MyUser.objects.create(nickname=nickname)

            auth_login(request, user)
            return redirect('maps:main')

    else:
        form = CustomUserCreationForm()
    context = {
        'signup_form': form,
    }
    return render(request, 'accounts/auth_form.html', context)

# 로그인
def login(request):
    if request.user.is_authenticated:
        return redirect('maps:main')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('maps:main')
    else:
        form = AuthenticationForm()
    context = {
        'login_form' : form, 
    }
    return render(request, 'accounts/auth_form.html', context)

# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('maps:main')

# 회원정보 수정 
@login_required
def update(request):
    if request.method == "POST":
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('accounts:mypage', request.user)
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
    context = {
        'user_change_form' : user_change_form, 
    }
    return render(request, 'accounts/auth_form.html', context)

# 회원 탈퇴
@login_required
def delete(request):
    if request.method == "POST":
        request.user.delete()
    return redirect('maps:main')

# 마이페이지
def mypage(request, username):
    myinfo = get_object_or_404(get_user_model(), username=username)
    context = {'myinfo': myinfo, }
    return render(request, 'accounts/mypage.html', context)

@api_view(['GET'])
def UserSerializer(request):
    '''
    모든 유저 정보
    '''
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def UserInfoserializer(request, email):
    '''
    email로 유저 정보 가져오기
    email로 유저 정보 삭제
    '''
    user = get_object_or_404(get_user_model(), email=email)
    serializer = SearchUserSerializer(user, many=True)
    return Response(serializer.data)