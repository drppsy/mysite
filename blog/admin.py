from django.contrib import admin
from blog.models import BlogType,Blog

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','blog_type','author','get_read_num','created_time','last_updated_time')

'''
方法1实现的admnin后台获取阅读计数
@admin.register(ReadNum)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('read_num','blog')
'''