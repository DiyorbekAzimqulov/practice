from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone


class Command(BaseCommand):
    help = "It shows current time"

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime("%X")
        self.stdout.write(f"It is now {time}")
