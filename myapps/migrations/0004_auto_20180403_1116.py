# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0003_auto_20180403_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='date_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='people_end',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
