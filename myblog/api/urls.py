from rest_framework import routers
from .api import CategoryViewSet, PostViewSet

router = routers.DefaultRouter()

router.register('api/categories', CategoryViewSet, 'Category')
router.register('api/posts', PostViewSet, 'Post')

urlpatterns = router.urls