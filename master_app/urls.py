from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/students/', views.StudentList.as_view()),
    path('api/student/<int:pk>/', views.StudentDetail.as_view()),

    path('api/hostels/', views.HostelList.as_view()),
    path('api/hostel/<int:pk>/', views.HostelDetail.as_view()),

    path('api/rooms/', views.RoomList.as_view()),
    path('api/room/<int:pk>/', views.RoomDetail.as_view()),

    path('api/wardens/', views.WardenList.as_view()),
    path('api/warden/<int:pk>/', views.WardenDetail.as_view()),

    path('api/Parents/', views.ParentList.as_view()),
    path('api/Parent/<int:pk>/', views.ParentDetail.as_view()),

    path('api/hostelfees/', views.HostelFeeList.as_view()),
    path('api/hostelfee/<int:pk>/', views.HostelFeeDetail.as_view()),


]
