from django.urls import path
from . import views
from django.conf.urls import url, include

app_name = 'maps'


urlpatterns = [
    
    path('', views.main, name='main'),
    path('map/', views.map, name="map"),
    path('map/update/', views.detailcommon, name="detailcommon"),
    path('korea/', views.korea, name='korea'),
    path('test/', views.test),

    ]