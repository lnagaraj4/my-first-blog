# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_conclusion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='conclusion',
        ),
    ]
