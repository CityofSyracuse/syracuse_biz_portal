# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-21 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biz_content', '0003_auto_20161121_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistitem',
            name='checklist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checklist_items', to='biz_content.Checklist'),
        ),
    ]
