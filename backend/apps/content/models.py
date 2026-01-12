import uuid
from django.db import models
from apps.programs.models import Lesson

class LessonTranslation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    language_code = models.CharField(max_length=10)
    title = models.TextField()
    body = models.TextField()
    is_complete = models.BooleanField(default=False)

    class Meta:
        unique_together = ('lesson', 'language_code')

