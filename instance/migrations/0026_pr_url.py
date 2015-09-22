# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from django.conf import settings


def migrate_urls(apps, schema_editor):
    Instance = apps.get_model("instance", "OpenEdXInstance")
    instances = Instance.objects.exclude(github_pr_number__isnull=True)
    for instance in instances:
        instance.github_pr_url = 'https://github.com/{fork}/pull/{number}'.format(
            fork=getattr(settings, 'WATCH_FORK', 'edx/edx-platform'),
            number=instance.github_pr_number
        )
        instance.save()


def reverse_migrate_urls(apps, schema_editor):
    Instance = apps.get_model("instance", "OpenEdXInstance")
    instances = Instance.objects.exclude(github_pr_url='')
    for instance in instances:
        instance.github_pr_number = int(instance.github_pr_url.split('/')[-1])
        instance.save()


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0025_openedxinstance_github_pr_url'),
    ]

    operations = [
        migrations.RunPython(migrate_urls, reverse_code=reverse_migrate_urls)
    ]
