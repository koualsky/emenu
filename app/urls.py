from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .api import CardViewSet, DishViewSet


router = DefaultRouter()
router.register(r'cards', CardViewSet)
router.register(r'dishes', DishViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
