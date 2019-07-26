from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('<str:username>/', views.mypage, name='mypage'),
    path('update/', views.update, name='update'),
    # path('change_password/', views.change_password, name='change_password'),
    path('delete/', views.delete, name='delete'),

    # API Link(Only Admin)
    path('user/', views.UserSerializer),
    path('user/<str:email>/', views.UserInfoserializer, name='UserInfo'),
    ]