from django.contrib import admin

# Register your models here.
from .models import Task         

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed', 'created_at')        # 列表显示
    list_filter = ('completed', 'created_at')                        # 右侧过滤器
    search_fields = ('title',)                                       # 搜索框
    ordering = ('-created_at',)                                      # 排序方式
    readonly_fields = ('created_at',)                                # 只读字段
admin.site.register(Task, TaskAdmin)