# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-06 13:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='news',
            new_name='news_topic',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='video',
            new_name='news',
        ),
    ]