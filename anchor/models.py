from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Anchor(models.Model):
    name = models.CharField(max_length=50,verbose_name="主播名称")
    room_id = models.CharField(max_length=255,verbose_name="房间号")
    guild_id = models.IntegerField(verbose_name="公会号")
    platform = models.CharField(max_length=50,verbose_name="平台名称")
    value_at = models.CharField(max_length=255,verbose_name="获取时间")
    follow = models.IntegerField(verbose_name="订阅数")
    redu = models.IntegerField(verbose_name="热度")
    section_id = models.IntegerField(verbose_name="版块ID")
    last_kaibo_at = models.CharField(max_length=255,verbose_name="上次开播时间")
    update_at = models.CharField(max_length=255,verbose_name="上次更新时间")
    is_noguild = models.CharField(max_length=20,verbose_name="有无公会")
    is_contact = models.CharField(max_length=20,verbose_name="是否联系过")
    uid = models.CharField(max_length=100)
    note = models.CharField(max_length=255,default="",verbose_name="备注")
    room_link = models.CharField(max_length=255,default="",verbose_name="房间链接")


    class Meta:
        verbose_name = "主播"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# class Notes(models.Model):
#     anchor_id = models.ForeignKey(Anchor,on_delete=models.DO_NOTHING)
#     note_content = models.CharField(max_length=255,default="",verbose_name="备注")
#     # admin_id = models.ForeignKey(User,on_delete=models.DO_NOTHING)
#
#
#     class Meta:
#         verbose_name = "备注"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
#

class AnchorGuild(models.Model):
    host_id = models.IntegerField(verbose_name="主播ID")
    guild_id = models.IntegerField(verbose_name="公会ID")
    value_at = models.CharField(max_length=255,verbose_name="获取时间")


class Guild(models.Model):
    value = models.CharField(max_length=30,verbose_name="")
    platform = models.CharField(max_length=30,verbose_name="平台名称")
    value_at = models.CharField(max_length=255)


class Section(models.Model):
    platform = models.CharField(max_length=30, verbose_name="平台名称")
    name = models.CharField(max_length=30, verbose_name="名称")