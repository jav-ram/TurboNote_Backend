from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nota
        exclude = []

class NotaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nota
        exclude = ['contenido', 'pertenece']

class AmistadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Amistad
        exclude = []

class CompartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Compartido
        exclude = []