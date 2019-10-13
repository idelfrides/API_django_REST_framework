from rest_framework.serializers import ModelSerializer
from adress.models import Adress


class AdressSerializer(ModelSerializer):
    class Meta:
        model = Adress
        fields = ['id', 'line1', 'city', 'state']