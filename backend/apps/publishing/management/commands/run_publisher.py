from django.core.management.base import BaseCommand
from apps.publishing.services.publisher import publish_scheduled_lessons

class Command(BaseCommand):
    help = "Publish scheduled lessons"

    def handle(self, *args, **kwargs):
        publish_scheduled_lessons()
        self.stdout.write("Publisher ran successfully")
