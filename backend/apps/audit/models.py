import uuid
from django.db import models
from apps.users.models import User

class AuditLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.TextField()
    entity_type = models.CharField(max_length=50)
    entity_id = models.UUIDField()
    before = models.JSONField(null=True)
    after = models.JSONField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

