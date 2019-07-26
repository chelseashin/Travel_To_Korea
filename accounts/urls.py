from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('<str:username>/', views.mypage, name='mypage'),
<<<<<<< HEAD
    path('update/', views.update, name='update'),
    # path('<str:nickname>/change_password/', views.change_password, name='change_password'),
    path('delete/', views.delete, name='delete')
=======

    # API Link(Only Admin)
    path('user/', views.UserSerializer),
    path('user/<str:email>/', views.UserInfoserializer, name='UserInfo'),
>>>>>>> fde0c8d8c4c29f8b6619fe789d1db951c2b945bc
    ]

