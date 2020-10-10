from django.urls import path
from . import api

urlpatterns = [
	path("/", api.test_endpoint, name="test")

]