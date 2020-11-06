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
from database.views import   BugReportAPI, SingleBugAPI, SearchBugAPI,CommentAPI, BugUserLikesAPI,SearchAssigneeAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

########## Authenticate route #######



urlpatterns = [
    path('', include(router.urls)),
	path('', include("database.urls")),
    path('', include("accounts.urls")),
    path('bugs', BugReportAPI.as_view(),name="addbugrpt"),
    path('bug/<int:pk>/', SingleBugAPI.as_view(),name="bug"),
    path('bug/search/', SearchBugAPI.as_view(), name='searchbug'),
    path('comment/<int:pk>/',CommentAPI.as_view()),
    path('buglikes/<int:pk>/',BugUserLikesAPI.as_view()),
    path('bug/assign_search/', SearchAssigneeAPI.as_view(),name='searchbugasn')

]


