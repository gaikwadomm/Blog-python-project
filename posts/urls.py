from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name = 'login'),
    path('login',views.login, name = 'login2'),
    path('logout', views.logout, name = 'logout'),
    path('delete/', views.delete, name = 'delete'),
    path('register', views.register, name = 'register'),
    path('index', views.index, name = 'index'),
    path('posts/<str:pk>',views.posts, name = 'post'),

]