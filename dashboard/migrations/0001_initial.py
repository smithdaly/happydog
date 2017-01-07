# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=200)),
                ('event_description', models.TextField()),
                ('event_date', models.DateField(default=django.utils.timezone.now)),
                ('event_time', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day_num', models.CharField(max_length=20)),
                ('time', models.IntegerField()),
                ('create_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Venu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('google_place_id', models.CharField(max_length=200)),
                ('venu_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('trading_hours', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='occupation',
            name='venu',
            field=models.ForeignKey(to='dashboard.Venu'),
        ),
        migrations.AddField(
            model_name='event',
            name='venu',
            field=models.ForeignKey(to='dashboard.Venu'),
        ),
    ]
