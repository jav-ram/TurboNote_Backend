from rest_framework import viewsets

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