# views.py
from rest_framework.mixins import (CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin)
from rest_framework.viewsets import GenericViewSet
from .models import Role, User, Bug
from .serializers import RoleSerializer, UserSerializer, BugSerializer


class BugViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Company
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin):  # handles GETs for many Companies

      serializer_class = BugSerializer
      queryset = Bug.objects.all()