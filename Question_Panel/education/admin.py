from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ["user", "note_title", "note_status", "date_created"]
    list_editable = ["note_status"]
    prepopulated_fields = {"slug": ("note_title",)}
    search_fields = ["user", "note_title", "note_status", "date_created"]
