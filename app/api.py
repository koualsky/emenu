from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Count
from .models import Card, Dish
from .serializers import CardSerializer, CardSerializerList, DishSerializer
from rest_framework.response import Response


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = Card.objects.all()

        # If we have some parameters in GET request
        if self.request.GET:

            # Filter by name
            queryset = queryset.order_by('name') if self.request.GET.get('name') == 'asc' else queryset
            queryset = queryset.order_by('-name') if self.request.GET.get('name') == 'desc' else queryset

            # Filter by dishes amount
            queryset = queryset.annotate(dishes__count=Count('dishes')).order_by(
                'dishes__count') if self.request.GET.get('dishes') == 'asc' else queryset
            queryset = queryset.annotate(dishes__count=Count('dishes')).order_by(
                '-dishes__count') if self.request.GET.get('dishes') == 'desc' else queryset

            # Filter by date (created_on)
            queryset = queryset.order_by('created_on') if self.request.GET.get('created_on') == 'asc' else queryset
            queryset = queryset.order_by('-created_on') if self.request.GET.get('created_on') == 'desc' else queryset

            # Filter by date (updated_on)
            queryset = queryset.order_by('updated_on') if self.request.GET.get('updated_on') == 'asc' else queryset
            queryset = queryset.order_by('-updated_on') if self.request.GET.get('updated_on') == 'desc' else queryset

        serializer = CardSerializerList(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
