from django.db import models
from category.models import Category


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def __str__(self):
        return self.title