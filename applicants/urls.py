from django.urls import path, re_path
from . import views

urlpatterns = [
  path('candidatos/', views.getAdd, name='candidatos'),
  path('candidatos/<int:id>', views.getUpdateDelete, name='candidatos por ID')
]