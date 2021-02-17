from rest_framework import serializers
from .models import Card, Dish


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class CardSerializer(serializers.HyperlinkedModelSerializer):
    dishes = DishSerializer(many=True, read_only=True)
    total_dishes = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = ('url', 'name', 'description', 'created_on', 'updated_on', 'total_dishes', 'dishes')

    @staticmethod
    def get_total_dishes(obj):
        return obj.dishes.count()


class CardSerializerList(serializers.HyperlinkedModelSerializer):
    total_dishes = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = ('url', 'name', 'description', 'created_on', 'updated_on', 'total_dishes')

    @staticmethod
    def get_total_dishes(obj):
        return obj.dishes.count()
