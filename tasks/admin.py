from django.contrib import admin
from django.template.defaultfilters import title

from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed',)
    list_filter =  ('title', 'completed', 'created_at',)
    search_fields = ('title', 'completed', 'created_at',)
