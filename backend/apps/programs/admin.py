from django.contrib import admin
from .models import Program, Term, Lesson


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_active", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "slug")
    list_filter = ("is_active",)
    ordering = ("-created_at",)


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ("title", "program", "order")
    list_filter = ("program",)
    ordering = ("program", "order")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("slug", "term", "status", "publish_at", "order")
    list_filter = ("status", "term__program")
    search_fields = ("slug",)
    ordering = ("term", "order")
    readonly_fields = ("created_at",)

    fieldsets = (
        ("Lesson Info", {
            "fields": ("term", "slug", "order")
        }),
        ("Publishing", {
            "fields": ("status", "publish_at")
        }),
        ("System", {
            "fields": ("created_at",)
        }),
    )
