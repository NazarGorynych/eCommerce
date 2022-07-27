from rest_framework import routers
from .views import UserViewSet, ProductViewSet, ProductCommentViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'productcomments', ProductCommentViewSet)
