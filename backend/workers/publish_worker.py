import django
import os
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.db import transaction
from django.utils import timezone
from apps.programs.models import Lesson
from apps.publishing.models import PublishLog


def run():
    print("📢 Publish worker started")

    while True:
        now = timezone.now()

        with transaction.atomic():
            lessons = (
                Lesson.objects
                .select_for_update(skip_locked=True)
                .filter(
                    status="scheduled",
                    publish_at__lte=now
                )
            )

            for lesson in lessons:
                log, created = PublishLog.objects.get_or_create(lesson=lesson)

                if log.published_at:
                    continue   # already published

                lesson.status = "published"
                lesson.save()

                log.published_at = now
                log.published_by_worker = True
                log.save()

                print(f"✅ Published: {lesson.slug}")

        time.sleep(30)   # check every 30 seconds


if __name__ == "__main__":
    run()
