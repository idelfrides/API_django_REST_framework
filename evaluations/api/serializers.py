from rest_framework.serializers import ModelSerializer
from evaluations.models import Evaluation


class EvaluationSerializer(ModelSerializer):    
    class Meta:
        model = Evaluation
        fields = ['id', 'user', 'comment', 'value', 'date']