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
from database.views import BugsController, BugController,SearchKeywordController,CommentController, BugStatusController,SearchAssigneeController,SearchTitleController,ViewWeeklyBugController,ViewMonthlyBugController
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
	path('', include("database.urls")),
    path('', include("accounts.urls")),
    path('bugs', BugsController.as_view(),name="addbugrpt"),
    path('bug/<int:pk>/', BugController.as_view(),name="bug"),
    path('bug/search/', SearchKeywordController.as_view(), name='searchbug'),
    path('comment/<int:pk>/',CommentController.as_view(),name='comment'),
    path('buglikes/<int:pk>/',BugStatusController.as_view()),
    path('bug/assign_search/', SearchAssigneeController.as_view(),name='searchbugasn'),
    path('bug/title_search/', SearchTitleController.as_view()),
    path('bug/monthly/', ViewMonthlyBugController.as_view()),
    path('bug/weekly/', ViewWeeklyBugController.as_view())

]


