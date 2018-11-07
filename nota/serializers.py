from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Note
        exclude = []

class NoteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Note
        exclude = ['body', 'owner']

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Friendship
        exclude = []

class SharedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shared
        exclude = []