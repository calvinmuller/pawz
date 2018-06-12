from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Organisation, Status, Paw, Breed, Colour, PawImage


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'is_staff', 'is_active', 'last_login', 'date_joined')


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name')


class BreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'name')


class ColourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Colour
        fields = ('id', 'name')


class PawImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PawImage
        fields = ('id', 'image')

class OrganisationSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    status = StatusSerializer()

    class Meta:
        model = Organisation
        fields = ('__all__')

class PawSerializer(serializers.HyperlinkedModelSerializer):
    organisation = OrganisationSerializer()
    breed = BreedSerializer()
    colour = ColourSerializer()
    status = StatusSerializer()

    images = PawImageSerializer(many=True, read_only=True)

    class Meta:
        model = Paw
        lookup_field = 'slug'
        fields = ('id', 'name', 'slug', 'organisation', 'status', 'breed', 'colour', 'picture', 'images', 'url')