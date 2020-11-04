from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Comment, Bug, User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
import json
from django.contrib.auth.models import User
from database.models import Profile
import string
import random

#http://localhost:8000/populate_users
@csrf_exempt
@require_http_methods(["GET"])
def users(req):
    def assign_expertise():
      random_no = random.randint(0,6)
      return random_no
    if(req.method == 'GET'):
      hash_passwd = make_password("123456")
      for i in range(1,36):
        user = User(username="user{}".format(i), email="user{}@gmail.com".format(i), password=hash_passwd)
        profile = Profile(user=user,role_title="user")
        user.save()
        profile.save()

      for i in range(35,41):
        user = User(username="developer{}".format(i), email="developer{}@gmail.com".format(i), password=hash_passwd)
        profile = Profile(user=user,role_title="developer",expertise=assign_expertise())
        user.save()
        profile.save()


      for i in range(40,46):
        user = User(username="triager{}".format(i), email="triager{}@gmail.com".format(i), password=hash_passwd)
        profile = Profile(user=user,role_title="triager")
        user.save()
        profile.save()


      for i in range(45,51):
        user = User(username="reviewer{}".format(i), email="reviewer{}@gmail.com".format(i), password=hash_passwd)
        profile = Profile(user=user,role_title="reviewer")
        user.save()
        profile.save()




      return HttpResponse({
        "succesfully populate"
      })


#http://localhost:8000/populate_bugs
@csrf_exempt
@require_http_methods(["GET"])
def bugs(req):
  def assign_priority():
    random_no = random.randint(0,4)
    priority = {
      1: "low",
      2: "medium",
      3: "high",
    }
    return(priority.get(random_no,None))

  def assign_developer():
    random_no = random.randint(0,41)
    if(random_no >35 and random_no<41):
      return random_no
    else:
      return None

  def assign_reported_by():
    random_no = random.randint(1,36)
    return random_no

  def assign_count():
    random_no = random.randint(0,14)
    return random_no


  def assign_status():
    random_no = random.randint(1,3)
    status = {
      1: "fixed",
      2: "active"
    }
    return(status.get(random_no,None))

  if(req.method == 'GET'):
      for i in range(1,501):
        developer_id = assign_developer()
        if(developer_id):
          developer = User.objects.get(id=developer_id)
        else:
          developer = None
        bug = Bug(id=i,name="bug{}".format(i),
        description="This is bug {}".format(i),
        status=assign_status(),
        priority=assign_priority(),
        upvote_count=assign_count(),
        reported_by_id=assign_reported_by(),
        developer_assigned=developer)
        bug.save()

  return HttpResponse({
        "succesfully populate bugs"
  })





