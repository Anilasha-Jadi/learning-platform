from django.contrib import admin
from .models import PublishLog

@admin.register(PublishLog)
class PublishLogAdmin(admin.ModelAdmin):
    list_display = ("lesson", "published_at", "published_by_worker")
    readonly_fields = ("lesson", "published_at", "published_by_worker")
    list_filter = ("published_by_worker",)

    def has_add_permission(self, request):
        # Prevent adding manually from admin
        return False
