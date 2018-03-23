from django.contrib.auth.models import User
from django.forms import CharField
from django.http import QueryDict
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets, generics, mixins
from rest_framework.decorators import list_route, api_view
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import UserIsOwnerOrReadOnly
from api.serializers import OrganisationSerializer, StatusSerializer, UserSerializer, PawSerializer
from core.models import Organisation, Status, Paw


class OrganisationViewSet(viewsets.ModelViewSet):
    permission_classes = (DjangoModelPermissions,)
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Organisation.objects.all().order_by('-date_created')
    serializer_class = OrganisationSerializer


class StatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSets define the view behavior.
class PawViewSet(viewsets.ModelViewSet):
    permission_classes = (DjangoModelPermissions,)

    queryset = Paw.objects.all().order_by('-created_at')
    serializer_class = PawSerializer


# currently logged in user
class CurrentUserViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, UserIsOwnerOrReadOnly)
    base_name = 'me'

    def list(self, request):
        serializer = UserSerializer(request.user, many=False)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # queryset = request.user
        user = request
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user = request.user
        first_name = request.data.get('first_name')
        last_name =  request.data.get('last_name')
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)
