from rest_framework.viewsets import ModelViewSet

from core.models import Acessorios
from core.serializers import AcessoriosSerializer


class AcessoriosViewSet(ModelViewSet):
    queryset = Acessorios.objects.all()
    serializer_class = AcessoriosSerializer
