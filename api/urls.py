from django.urls import include, path
from .routers import router

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
]
