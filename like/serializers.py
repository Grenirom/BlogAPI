from rest_framework import serializers
from .models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        fields = '__all__'
        model = Favorite

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        return repr['post']
    