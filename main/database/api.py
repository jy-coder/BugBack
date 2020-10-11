from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import  Role, Comment, Bug, User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
import json
from django.contrib.auth.models import User
import string


### Populate database method -this should only be run once###
@csrf_exempt
@require_http_methods(["GET"])
def test_endpoint(req):
    
    hash_passwd = make_password("123456")

    for i in range(1,15):
        #save pw , email, username
        user = User(id=i,username="test{}".format(i), 
        email="test{}@gmail.com".format(i), password=hash_passwd) 
        user.save()
        print(user)
    


    return HttpResponse({
      "succesfully populated"
    })

    

