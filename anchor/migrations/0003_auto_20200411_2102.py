# Generated by Django 2.2.6 on 2020-04-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anchor', '0002_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='anchor',
            name='note',
            field=models.CharField(default='', max_length=255, verbose_name='备注'),
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
    ]
