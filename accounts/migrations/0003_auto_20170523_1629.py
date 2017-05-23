# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='subject',
            field=models.CharField(default=b'standupmeeting', max_length=30, blank=True),
        ),
    ]
