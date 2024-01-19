from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import ProfileModel
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        read_only_fields =('id',)
        exclude = ('user',)