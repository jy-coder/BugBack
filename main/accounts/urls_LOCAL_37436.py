from django.urls import path, include
from .api import RegisterAPI, LoginController, UserController, SingleUserController
from knox import views as knox_views

urlpatterns = [
  path('api/auth', include('knox.urls')),
  path('api/auth/register', RegisterAPI.as_view()),
  path('api/auth/login', LoginController.as_view(), name='login'),
  path('api/auth/user', UserController.as_view(), name='users'),
  path('api/auth/user/<int:pk>', SingleUserController.as_view()),
  path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout')
]