from django.urls import re_path, path, include

from . import views
from .views import schema_view
from web import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
  re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
  
  path("", views.index),
  
    
  path('workers/', views.WorkersListView.as_view()),
  path('workers/<int:id>/', views.WorkersListView.as_view()),
  path('entrances/', views.EntranceListView.as_view()),
  path('entrances/<int:id>/', views.EntranceListView.as_view()),
  
  
  path("api-auth/", include("rest_framework.urls")), 
  path('rest-auth/', include('dj_rest_auth.urls')),
  
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)