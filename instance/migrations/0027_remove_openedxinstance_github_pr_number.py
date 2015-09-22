# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0026_pr_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openedxinstance',
            name='github_pr_number',
        ),
    ]
