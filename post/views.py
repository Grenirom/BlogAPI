from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import PostSerializer
from rest_framework.response import Response
from .models import Post 
from .permission import IsOwner


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method in ['GET', 'POST']:
            return [IsAuthenticated(), ]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser(), IsOwner()]
        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
