# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-27 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_announcement_is_urgent'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='name',
            field=models.CharField(default='marvo', max_length=100),
            preserve_default=False,
        ),
    ]