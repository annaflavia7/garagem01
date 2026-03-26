from rest_framework.viewsets import ModelViewSet

from core.models.modelo import Modelo
from core.serializers.modelo import ModeloSerializer


class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
