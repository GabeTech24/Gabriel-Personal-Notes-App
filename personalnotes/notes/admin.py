from django.contrib import admin
from .models import Notes

# Register your models here.

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    list_filter = ['title']
