# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170523_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(default=b'productmanager', max_length=30, blank=True),
        ),
    ]
