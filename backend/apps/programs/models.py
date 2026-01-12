import uuid
from django.db import models
from django.utils import timezone

class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["slug"]),
        ]

    def __str__(self):
        return self.title


class Term(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="terms")
    slug = models.SlugField(max_length=255)
    title = models.CharField(max_length=255, null=True, blank=True)
    order = models.PositiveIntegerField(null=True, blank=True)


    class Meta:
        unique_together = ("program", "order")
        ordering = ["order"]

    def __str__(self):
        return f"{self.program.title} → {self.title}"


class Lesson(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("scheduled", "Scheduled"),
        ("published", "Published"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name="lessons")

    slug = models.SlugField(null=True, blank=True, db_index=True)
    order = models.PositiveIntegerField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")

    publish_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(null=True, blank=True)



    class Meta:
        unique_together = ("term", "slug")
        ordering = ["order"]
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["publish_at"]),
        ]

    def is_publishable(self):
        return self.status == "scheduled" and self.publish_at and self.publish_at <= timezone.now()

    def __str__(self):
        return f"{self.term} → {self.slug}"
