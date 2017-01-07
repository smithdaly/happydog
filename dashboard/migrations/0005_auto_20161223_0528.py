# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20161222_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
