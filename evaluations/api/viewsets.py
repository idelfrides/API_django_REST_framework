from rest_framework.viewsets import ModelViewSet
from evaluations.models import Evaluation
from .serializers import EvaluationSerializer


class EvaluationViewSet(ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
