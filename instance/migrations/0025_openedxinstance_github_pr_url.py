# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0024_auto_20150911_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='openedxinstance',
            name='github_pr_url',
            field=models.CharField(blank=True, max_length=200, default=''),
        ),
    ]
