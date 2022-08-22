from django.urls import re_path, path

from . import views
from .views import schema_view

urlpatterns = [
  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
  re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
    
  path('workers/', views.WorkersListView.as_view()),
  path('workers/<int:id>/', views.WorkersListView.as_view()),
]