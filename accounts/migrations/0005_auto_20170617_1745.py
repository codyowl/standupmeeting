# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sender_email',
            field=models.EmailField(default=datetime.datetime(2017, 6, 17, 17, 45, 9, 188179, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='sender_email_password',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
    ]
