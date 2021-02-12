from rest_framework.viewsets import ModelViewSet
from .models import Card, Dish
from .serializers import CardSerializer, DishSerializer


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
