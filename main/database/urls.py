from django.urls import path
from . import api

urlpatterns = [
	path('populate_users', api.users, name="populate_users"),
	path('populate_bugs', api.bugs, name="populate_bugs")
]