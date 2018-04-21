# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0002_auto_20180403_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='date_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='people_end',
            field=models.CharField(null=True, max_length=50),
        ),
    ]
