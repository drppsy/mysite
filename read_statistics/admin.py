from django.contrib import admin
from read_statistics.models import ReadNum,ReadDetail

@admin.register(ReadNum)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('read_num','content_object')

@admin.register(ReadDetail)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('date','read_num','content_object')
