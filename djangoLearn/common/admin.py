from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from .models import Customer, TestModel


# class CustomAdminSite(AdminSite):
#     site_header = '我的管理后台'
#     site_title = '后台管理'
#     index_title = '数据仪表盘'
    
#     def get_app_list(self, request):
#         # 自定义首页显示顺序
#         app_list = super().get_app_list(request)
#         # 重新排序app
#         return app_list
# admin.site = CustomAdminSite(name='myadmin')
admin.site.site_header = _('网站管理后台')  # 设置后台标题
admin.site.site_title = _('网站管理')     # 设置浏览器标签页标题
admin.site.index_title = _('后台管理')    # 设置首页标题



class TestModelStackedInline(admin.StackedInline):
    model = TestModel    # 关联子对象（多类对象）
    extra = 2  # 控制新增表单的数量
    # fk_name = 'customer'  # 明确指定外键字段名


class CustomerAdmin(admin.ModelAdmin):
    
    inlines = [TestModelStackedInline]   # 添加子对象

    def get_queryset(self, request):
        # 简化查询逻辑
        # get_queryset 的 only() 方法作用是后台性能优化，
        # 不会改变用户界面的显示内容。这种优化对于提升系统整体性能非常重要，尤其是在处理大量数据时。
        return super().get_queryset(request).only('id', 'name', 'phonenumber', 'address', 'email', 'created_date')
    
    """ 列表页选项 """    
    # 每页显示条数-默认为100
    list_per_page = 6

    # 显示字段
    list_display = ['id', 'name', 'phonenumber', 'address', 'email', 'created_date']

    # 只读字段
    readonly_fields = ['id']

    # 列表页字段编辑
    list_editable = ['phonenumber']

    # 列表页字段搜索
    search_fields = ['name', 'phonenumber']

    # 日期层级筛选
    date_hierarchy = 'created_date'  # 日期字段

    # 列表页字段排序
    ordering = ['id']

    # 列表页字段筛选-过滤器
    list_filter = ['name', 'phonenumber']

    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True

    """ 编辑页选项 """
    # 编辑页字段排序  -- 默认是按照字段定义的顺序  --  和 编辑页字段分组 fieldsets = () 冲突不能同时使用
    # fields = ['email', 'phonenumber', 'address', 'name', 'created_date']

    # 编辑页字段分组
    fieldsets = (
        ('基本信息', {
            "fields": ('name', 'address'),   
            # 'classes': ('collapse',)      # 折叠字段
            }
        ),
        ('其他信息', {"fields": ('phonenumber', 'email')}),
    )

    # save_model 是 ModelAdmin 类中的一个方法，它在用户点击"保存"按钮时被调用。这个方法允许你在保存数据之前或之后执行额外的操作。
    def save_model(self, request, obj, form, change):
        print("do something")
        super().save_model(request, obj, form, change)

    """ 自定义批量操作 """
    """ 演示无实际功能 """
    actions = ['make_export', 'bulk_update_address']
    def make_export(self, request, queryset):
        # 导出选中数据
        count = queryset.count()
        self.message_user(request, f'成功导出 {count} 条客户数据', messages.SUCCESS)
    make_export.short_description = "导出选中"

    def bulk_update_address(self, request, queryset):
        # 批量更新地址
        queryset.update(address='地址待更新')
        self.message_user(request, f'已更新 {queryset.count()} 条地址')
    bulk_update_address.short_description = "批量更新地址"

admin.site.register(Customer, CustomerAdmin)




class TestModelAdmin(admin.ModelAdmin):
    # 每页显示条数-默认为100
    list_per_page = 5
    # 显示字段
    list_display = ['id', 'status', 'customer']
admin.site.register(TestModel, TestModelAdmin)