from django.contrib import admin
from .models import Project, Task

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # This creates a professional table view for your tasks
    list_display = ('title', 'project', 'priority', 'status', 'created_at')
    
    # This adds the sidebar filters for quick navigation
    list_filter = ('status', 'priority', 'project')
    
    # This allows for quick search by title
    search_fields = ('title',)

    # Optional: Automatically display the order of tasks
    ordering = ('-created_at',)