from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from cuaderno.permissions import IsOwnerOrReadOnly
from . import models, serializers
from nota import models as modelNota, serializers as NotaSerializer
# Create your views here.

class NotebookModelViewSet(viewsets.ModelViewSet):
    # /cuaderno/ devuelve todo 
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = models.Notebook.objects.all()
    serializer_class = serializers.NotebookSerializer

    @action(methods=['GET'], detail=True, url_path='all-notes')
    # /cuaderno/all-notes/ devuelve todas las NOTAS dentro de del cuaderno
    def all_notes(self, request, pk=None):
        notebook = self.get_object()
        notes = modelNota.Note.objects.filter(owner = notebook.pk)
        notes_serialize = NotaSerializer.NoteItemSerializer(notes, many=True)

        return Response(
            notes_serialize.data
        )

class UserPermissions(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        return request.user and request.user.is_authenticated

class UserModelViewSet(viewsets.ModelViewSet):
    permission_classes = (UserPermissions, )
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @action(methods=['GET'], detail=True, url_path='all-notebooks')
    # /usuario/all-notebooks/ devuelve todos los CUADERNOS del usuario
    def all_notebooks(self, request, pk=None):
        usuario = self.get_object()
        notebooks = models.Notebook.objects.filter(owner = usuario.pk)
        notebooks_serialize = serializers.NotebookSerializer(notebooks, many= True)

        return Response(
            notebooks_serialize.data
        )

    @action(methods=['GET'], detail=True, url_path='all-notes-from')
    # /usuario/all-notebooks/ devuelve todos los CUADERNOS del usuario
    def all_notebooks_from(self, request, pk=None):
        usuario = self.get_object()
        usuario_serialize = serializers.UserSerializer(usuario)

        friend = User.objects.get(pk=request.query_params['id'])
        friend_serializer = serializers.UserSerializer(friend)

        # verificar la amistad falta
        if (modelNota.Friendship.objects.filter(friend1=usuario, friend2=friend).count() > 0) or (modelNota.Friendship.objects.filter(friend1=friend, friend2=usuario).count() > 0):
            # son amigos 
            # get todos las notas
            shares = modelNota.Shared.objects.filter(owner=friend)
            notes = []

            for share in shares:
                pk_id = share.pk
                notes.append(modelNota.Note.objects.get(pk=pk_id))

            notes_serialize = NotaSerializer.NoteSerializer(notes, many=True)
            return Response( notes_serialize.data )
        else:
            return Response( {'error': "no son amigos"} )


        return Response(
            {"usuario" : usuario_serialize.data, "amigo":  friend_serializer.data}
        )
    
        
        