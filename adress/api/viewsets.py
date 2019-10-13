from rest_framework.viewsets import ModelViewSet
from .serializers import AdressSerializer
from adress.models import Adress


class AdressViewSet(ModelViewSet):
    queryset = Adress.objects.all()
    serializer_class = AdressSerializer
    