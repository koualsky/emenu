from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)    # Create date if object is created. Can't update this field.
    updated_on = models.DateTimeField(auto_now=True)        # Update this field with every save method on this object.


class Dish(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    preparation_time = models.TimeField()
    is_vegetarian = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)    # Create date if object is created. Can't update this field.
    updated_on = models.DateTimeField(auto_now=True)        # Update this field with every save method on this object.
