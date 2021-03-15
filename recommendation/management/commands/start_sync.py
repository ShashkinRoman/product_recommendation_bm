from django.core.management.base import BaseCommand
from recommendation.start_rec import start_synchronization_model


class Command(BaseCommand):
    help = 'start script for input'

    def handle(self, *args, **options):
        start_synchronization_model()
