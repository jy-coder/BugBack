from django.urls import path, include
from .api import RegisterAPI, LoginController, UserController, SingleUserController, DeveloperController
from knox import views as knox_views

urlpatterns = [
  path('api/auth', include('knox.urls')),
  path('api/auth/register', RegisterAPI.as_view()),
<<<<<<< HEAD
  path('api/auth/login', LoginController.as_view(), name='login'),
=======
  path('api/auth/login', LoginController.as_view(),name='login'),
>>>>>>> 4b8640bf928cf58ee777a4ce4820a2a0b212d692
  path('api/auth/user', UserController.as_view(), name='users'),
  path('api/auth/user/<int:pk>', SingleUserController.as_view()),
  path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
  path('api/developer', DeveloperController.as_view())
]