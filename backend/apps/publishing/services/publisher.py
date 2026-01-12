from django.utils import timezone
from apps.programs.models import Lesson
from apps.publishing.models import PublishLog

def publish_scheduled_lessons():
    now = timezone.now()

    lessons = Lesson.objects.filter(
        status="scheduled",
        publish_at__lte=now
    )

    for lesson in lessons:
        lesson.status = "published"
        lesson.save(update_fields=["status"])

        PublishLog.objects.update_or_create(
            lesson=lesson,
            defaults={
                "published_at": now,
                "published_by_worker": True
            }
        )
