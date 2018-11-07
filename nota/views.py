from rest_framework import viewsets

from . import models, serializers

# Create your views here.
class NoteModelViewSet(viewsets.ModelViewSet):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer

class FriendshipModelViewSet(viewsets.ModelViewSet):
    queryset = models.Friendship.objects.all()
    serializer_class = serializers.FriendSerializer

class SharedModelViewSet(viewsets.ModelViewSet):
    queryset = models.Shared.objects.all()
    serializer_class = serializers.SharedSerializer