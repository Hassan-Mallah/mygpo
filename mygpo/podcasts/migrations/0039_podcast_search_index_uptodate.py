# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-22 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0038_podcast_search_vector'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='search_index_uptodate',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
