from django.conf.urls import url
from django.urls import path, include

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from api.views import OrganisationViewSet, StatusViewSet, UserViewSet, PawViewSet, CurrentUserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'organisations', OrganisationViewSet)
router.register(r'me', CurrentUserViewSet, base_name='me')
router.register(r'status', StatusViewSet)
router.register(r'paws', PawViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/login', obtain_jwt_token),
    url(r'^auth/refresh', refresh_jwt_token)
]
