from rest_framework.serializers import ModelSerializer
from attraction.models import Attraction

class AttractionSerializer(ModelSerializer):
    """ Atracao serializer """

    class Meta:
        model = Attraction
        fields = ['id', 'name', 'description', 'opening_hours', 'minimum_age']