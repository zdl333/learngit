# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribute',
            name='distribute_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='date_end',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='people_end',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
