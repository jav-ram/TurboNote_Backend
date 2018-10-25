from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nota
        exclude = []

class AmistadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Amistad
        exclude = []

class CompartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Compartido
        exclude = []