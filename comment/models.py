from django.conf import settings

from django.db import models


class Comment(models.Model):
    '''
    User can write comments in a specific topic
    '''
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(
        'topic.Topic',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'comments'


class UserComment(models.Model):
    '''
    A through table for many-to-many relationship
    '''
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    comment = models.ForeignKey(
        'Comment',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'users_comments'
