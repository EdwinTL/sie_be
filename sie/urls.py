"""sie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from appSie import views


urlpatterns = [
path('login/', TokenObtainPairView.as_view()),
path('refresh/', TokenRefreshView.as_view()),
path('user/', views.UserCreateView.as_view()),
path('user/<int:pk>/', views.UserDetailView.as_view()),
path('grade/', views.GradeCreateView.as_view()),
path('grade/<pk>/', views.GradeDetailView.as_view()),
path('grade/update/<pk>/', views.GradeUpdateView.as_view()),
path('grade/remove/<pk>/', views.GradeDeleteView.as_view()),
path('group/', views.GroupCreateView.as_view()),
path('group/<int:pk>/', views.GroupDetailView.as_view()),
path('group/remove/<int:pk>/', views.GroupDeleteView.as_view()),
path('student/', views.StudentCreateView.as_view()),
path('student/<int:pk>/', views.StudentDetailView.as_view()),
path('student/remove/<int:pk>/', views.StudentDeleteView.as_view()),
path('subject/', views.SubjectCreateView.as_view()),
path('subject/remove/<int:pk>/', views.SubjectDeleteView.as_view()),
]


