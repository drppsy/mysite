from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod,ReadDetail

class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

class Blog(models.Model,ReadNumExpandMethod):
    # 定义Blog类的属性（title,blog_type,content,author,created_time,last_updated_time),也就是设计blog这张表（字段的数据类型、数据关系）

    # 定义标题title，CharField数据类型，字符长度上限是50
    title = models.CharField(max_length=50)
    # 定义blog_type属性，该属性是一个外键（ForeignKey），主键是BlogType这个类的实例化对象。注意，w外键（ForeignKey）是一对多的关系，外键放在“多”的一方
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    # 定义文本数据类型是RichTextUploadingField，支持图片上传
    content = RichTextUploadingField()
    # 定义作者属性，该属性也是一个外键对应的实例化对象
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    #
    read_details = GenericRelation(ReadDetail)
    # 定义创建时间，自动设置为now
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now_add=True)

    '''
    方法1——在blog应用中创建统计阅读数的方法
    # 定义Blog类的方法read-num，该方法从另一个OneToOneField的类/表readnum中，取得read_num的属性，如果没有该属性，那就捕获错误并返回0
    def get_read_num(self):
        try:
            return self.readnum.read_num
        except exceptions.ObjectDoesNotExist as e:
            return 0
    '''

    '''
    # 方法2——将统计阅读数封装成各个应用能调用的方法
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self) #self是具体的/实例化的一个blog对象
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist as e:
            return 0
    '''


    # 定义Blog类返回实例化对象title的方法
    def __str__(self):
        return "<Blog: %s>" % self.title
    # 定义Blog类的元数据，实例化对象以创建时间（created_time）倒序排序
    class Meta():
        ordering = ["-created_time"]

'''
方法1所需要的类/表
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    # 定义“一对一”的外键，代表一对一的数据关系
    blog = models.OneToOneField(Blog,on_delete=models.DO_NOTHING)
'''