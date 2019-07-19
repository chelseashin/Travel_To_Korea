from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [
    path('', views.main, name='main'),
    path('korea/', views.korea, name='korea'),
    path('detail/<int:content_id>/', views.detailpage),
    ]