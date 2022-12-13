from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name='login'),
    path("register/", views.registerPage, name='register'),
    path("logout/", views.logoutUser, name='logout'),
    path("", views.home, name='home'),
    path("room/<str:pk>/", views.room, name='room'),
    path('profile/<str:pk>', views.userProfile, name='user-profile'),
    path('createRoom/', views.createRoom, name='create-room'),
    path('updateRoom/<str:pk>/', views.updateRoom, name='update-room'),
    path('deleteRoom/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('deleteMessage/<str:pk>/', views.deleteMessage, name='delete-message'),
]