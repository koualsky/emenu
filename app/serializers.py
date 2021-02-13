from rest_framework import serializers
from .models import Card, Dish


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class CardSerializer(serializers.HyperlinkedModelSerializer):
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        # fields = '__all__'
        fields = ('name', 'description', 'created_on', 'updated_on', 'dishes')
