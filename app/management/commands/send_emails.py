from datetime import date, timedelta

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.db.models import Q
from app.models import Card, Dish


class Command(BaseCommand):
    help = 'Send email to all users with ...'

    def handle(self, *args, **options):

        # Get only last created or updated Dish
        yesterday = date.today() - timedelta(days=6)
        dishes = Dish.objects.filter(Q(created_on__date=yesterday) | Q(updated_on__date=yesterday))

        email = 'Last added dishes (yesterday):\n'
        for dish in dishes:
            email += f'{dish.name}\n'

        # Email body for send
        print(email)

        # Send email to all users
        '''
        User = get_user_model()
        users = User.objects.all()
        for user in users:
            print(user.email)
        '''
