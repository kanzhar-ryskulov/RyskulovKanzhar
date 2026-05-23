from django.contrib import admin

from to_do.models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'date')
    list_filter = ('status',)
    ordering = ('status',)