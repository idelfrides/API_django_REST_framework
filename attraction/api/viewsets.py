from rest_framework.viewsets import ModelViewSet
from attraction.models import Attraction
from .serializers import AttractionSerializer

class AttractionViewSet(ModelViewSet):

    """ Attraction serializer """
    
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

    
