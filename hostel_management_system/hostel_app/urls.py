from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.UserList.as_view()),
    path('api/user/<int:pk>/', views.UserDetail.as_view()),

]

