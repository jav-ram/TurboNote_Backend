from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models, serializers
from nota import models as modelNota, serializers as NotaSerializer
# Create your views here.


class CuadernoModelViewSet(viewsets.ModelViewSet):
    # /cuadeno/ devuelve todo 
    queryset = models.Cuaderno.objects.all()
    serializer_class = serializers.CuadernoSerializer

    @action(methods=['GET'], detail=True, url_path='all-notes')
    # /cuaderno/all-notes/ devuelve todas las NOTAS dentro de del cuaderno
    def all_notes(self, request, pk=None):
        cuaderno = self.get_object()
        notes = modelNota.Nota.objects.filter(pertenece = cuaderno.pk)
        notes_serialize = NotaSerializer.NotaItemSerializer(notes, many=True)

        return Response(
            notes_serialize.data
        )

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @action(methods=['GET'], detail=True, url_path='all-notebooks')
    # /usuario/all-notebooks/ devuelve todos los CUADERNOS del usuario
    def all_notebooks(self, request, pk=None):
        usuario = self.get_object()
        notebooks = models.Cuaderno.objects.filter(owner = usuario.pk)
        notebooks_serialize = serializers.CuadernoSerializer(notebooks, many= True)

        return Response(
            notebooks_serialize.data
        )