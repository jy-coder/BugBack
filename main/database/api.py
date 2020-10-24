from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Role, Comment, Bug, User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
import json
from django.contrib.auth.models import User
from database.models import Profile
import string


### Populate database method -this should only be run once###
@csrf_exempt
@require_http_methods(["GET", "DELETE"])
def test_endpoint(req):
    

    if(req.method == 'GET'):
      hash_passwd = make_password("123456")
      user = User(id=6,username="developer2", email="developer2@gmail.com", password=hash_passwd)
      profile = Profile(user=user,role_title="developer")
      user.save()
      profile.save()
      # user = User(id=1,username="user", email="user@gmail.com", password=hash_passwd)
      # profile = Profile(user=user,role_title="user")
      # user.save()
      # profile.save()
      # user = User(id=2,username="developer", email="developer@gmail.com", password=hash_passwd)
      # profile = Profile(user=user,role_title="developer")
      # user.save()
      # profile.save()
      # user = User(id=3,username="triager", email="triager@gmail.com", password=hash_passwd)
      # profile = Profile(user=user,role_title="triager")
      # user.save()
      # profile.save()
      # user = User(id=4,username="reviewer", email="reviewer@gmail.com", password=hash_passwd)
      # profile = Profile(user=user,role_title="reviewer")
      # user.save()
      profile.save()

      # user = User(id=1,username="user1", email="user1@gmail.com", password=hash_passwd) 
      # user = User(id=1,username="user1", email="user1@gmail.com", password=hash_passwd) 
      # user = User(id=1,username="user1", email="user1@gmail.com", password=hash_passwd) 
      # for i in range(1,15):
      #     #save pw , email, username
      #     user = User(id=i,username="test{}".format(i), 
      #     email="test{}@gmail.com".format(i), password=hash_passwd) 
      #     user.save()
      #     print(user)
      # for i in range(1,5):
      #     #save pw , email, username
      #     user = User(id=i,username="developer{}".format(i), 
      #     email="developer{}@gmail.com".format(i), password=hash_passwd) 
      #     user.save()
      #     print(user)


      return HttpResponse({
        "succesfully populate"
      })


    if(req.method == 'DELETE'):
        User.objects.get(id=1).delete()
        
        return HttpResponse({
          "succesfully deleted"
        })

    

