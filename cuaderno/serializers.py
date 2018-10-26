from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class CuadernoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cuaderno
        exclude = []

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']