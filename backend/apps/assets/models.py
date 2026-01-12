import uuid
from django.db import models
from apps.users.models import User
from apps.programs.models import Lesson

class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    file_url = models.TextField()
    file_type = models.CharField(max_length=20)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class LessonAsset(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
