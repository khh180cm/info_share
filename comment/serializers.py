from django.db import models
from rest_framework import serializers

from comment.models import Comment


class CommentSerializer(serializers.Serializer):
    '''Serialize comment objects to json representation'''
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic = serializers.RelatedField(source='topic', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
