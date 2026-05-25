from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at')
    list_filter = ('completed',)
    search_fields = ('title',)
    
    @admin.action(description='标记为已完成')
    def mark_completed(self, request, queryset):
        queryset.update(completed=True)
        
    actions = [mark_completed]

admin.site.register(Task, TaskAdmin)