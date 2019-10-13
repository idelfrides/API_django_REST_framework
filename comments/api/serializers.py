from rest_framework.serializers import ModelSerializer
from comments.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'the_comment', 'date', 'status']