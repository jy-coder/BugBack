from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import  Role, Comment, Bug

from django.http import HttpResponse, JsonResponse
import json

@csrf_exempt
@require_http_methods(["GET"])
def test_endpoint(req):
    return HttpResponse(json.dumps("abcd"))
    

