from rest_framework import serializers
from . import models

class CuadernoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cuaderno
        exclude = []