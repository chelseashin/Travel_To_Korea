from django.urls import path
from . import views
from django.conf.urls import url, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'maps'

# schema_url_v1_patterns = [
#     url(r'^v1/', include('maps.urls', namespace='map_api')),
# ]

schema_view = get_schema_view(
   openapi.Info(
      title="여행 API",
      default_version='v1',
      description="여기는 여행 api 문서 페이지입니다.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="injeong319@gmail.com"),
      license=openapi.License(name="ssafy's dif"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
#    patterns=schema_url_v1_patterns,
)

urlpatterns = [
    # url(r'^v1/', include('maps.urls', namespace='maps_api')),
    
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('', views.main, name='main'),
    path('map/', views.map, name="map"),
    path('korea/', views.korea, name='korea'),
    path('detail/<int:content_id>/', views.detailpage),
    # path('docs/', get_swagger_view(title="여행 정보 API")),

    ]