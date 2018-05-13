# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0004_auto_20180403_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribute',
            name='dis_type',
            field=models.CharField(max_length=10, default=1),
            preserve_default=False,
        ),
    ]
