import uuid
from django.db import models
from django.utils import timezone

class PublishLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    lesson = models.OneToOneField(
        "programs.Lesson",
        on_delete=models.CASCADE,
        related_name="publish_log"
    )

    published_at = models.DateTimeField(null=True, blank=True)
    published_by_worker = models.BooleanField(default=False)

    def __str__(self):
        return f"{getattr(self.lesson, 'title', self.lesson.id)} → {self.published_at}"

