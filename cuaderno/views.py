from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models, serializers
from nota import models as modelNota, serializers as NotaSerializer
# Create your views here.


class CuadernoModelViewSet(viewsets.ModelViewSet):
    queryset = models.Cuaderno.objects.all()
    serializer_class = serializers.CuadernoSerializer

    @action(methods=['GET'], detail=True, url_path='all-notes')
    def all_notes(self, request, pk=None):
        cuaderno = self.get_object()
        notes = modelNota.Nota.objects.filter(pertenece = cuaderno.pk)
        notesSerialize = NotaSerializer.NotaSerializer(notes, many=True)

        return Response({
            'message': notesSerialize.data
        })