from django.urls import path
from . import api

urlpatterns = [
	path('test', api.test_endpoint, name="test")

]