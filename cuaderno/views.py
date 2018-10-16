from rest_framework import viewsets
from . import models, serializers
# Create your views here.


class CuadernoModelViewSet(viewsets.ModelViewSet):
    queryset = models.Cuaderno.objects.all()
    serializer_class = serializers.CuadernoSerializer