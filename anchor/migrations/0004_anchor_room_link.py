# Generated by Django 2.2.6 on 2020-04-17 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anchor', '0003_auto_20200411_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='anchor',
            name='room_link',
            field=models.CharField(default='', max_length=255, verbose_name='房间链接'),
        ),
    ]