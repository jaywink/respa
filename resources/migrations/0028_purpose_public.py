# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0027_comments_verbose_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='purpose',
            name='public',
            field=models.BooleanField(default=True, verbose_name='Public'),
        ),
    ]
