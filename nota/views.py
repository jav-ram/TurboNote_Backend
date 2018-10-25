from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models, serializers

# Create your views here.

class NotaModelViewSet(viewsets.ModelViewSet):
    queryset = models.Nota.objects.all()
    serializer_class = serializers.NotaSerializer

class AmistadModelViewSet(viewsets.ModelViewSet):
    queryset = models.Amistad.objects.all()
    serializer_class = serializers.AmistadSerializer

class CompartidoModelViewSet(viewsets.ModelViewSet):
    queryset = models.Compartido.objects.all()
    serializer_class = serializers.CompartidoSerializer