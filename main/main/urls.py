"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from database.views import RoleViewSet, BugListAPI, AddBugReportAPI, BugReportAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'roles', RoleViewSet, basename='role')

########## Authenticate route #######



urlpatterns = [
    path('', include(router.urls)),
	path('', include("database.urls")),
    path('', include("accounts.urls")),
    path('bugs', BugListAPI.as_view()),
    path('addbugreport', AddBugReportAPI.as_view()),
    path('bugreport/<int:id>/', BugReportAPI.as_view()),
    # path('bugs/<int:pk>', BugSingleAPI.as_view()),

]


