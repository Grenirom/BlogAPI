from django.db import models
from post.models import Post


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='comments'
    )

