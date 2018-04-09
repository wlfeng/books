# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='user_name',
            field=models.CharField(max_length=20, verbose_name='用户名', unique=True),
        ),
    ]
