from .models import Category, Post
from rest_framework import viewsets, permissions
from .serializers import CategorySerializer, PostSerializer

# ViewSet for Category

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer