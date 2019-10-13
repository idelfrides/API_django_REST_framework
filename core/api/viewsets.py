from rest_framework.viewsets import ModelViewSet
from .serializers import TouristSpotSerializer
from core.models import TouristSpot
from rest_framework.response import Response


class TouristSpotViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing TouristSpot.
    """
    serializer_class = TouristSpotSerializer

    def get_queryset(self):
        """ get_queryset """
        return TouristSpot.objects.filter(aproved=True)
        
        # NOTE:
        # removed the queryset variable, it required to 
        # inform the base_name on the url register to define which class
        # it goint ot call

    # under the root
    def list(self, request, *args, **kwargs):
        """ Método de listagem geral (GET) do django REST
        sobre-escrito. --> http://127.0.0.1:8000/touristspots/
        """
        x = """ Método de listagem geral (GET) do django REST sobre-escrito """
        
        return Response({"test": x})

    def create(self, request, *args, **kwargs):
        pass

    # papaijorgeamkp19

