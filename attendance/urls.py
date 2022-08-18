from django.urls import path

from . import views

urlpatterns = [
  path('employers/', views.EmployersListView.as_view()),
  path('employers/<int:id>/', views.EmployersListView.as_view()),
]