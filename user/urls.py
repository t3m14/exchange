from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('verify/', views.verify, name='verify'),
    path('register/', views.register, name='register'),
    path('verify/documents/', views.documents, name='documents'),
]