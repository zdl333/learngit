# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distribute',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('text', models.TextField()),
                ('distribute_time', models.CharField(max_length=50)),
                ('distribute_people', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_start', models.DateTimeField(auto_now_add=True)),
                ('date_end', models.DateTimeField(auto_now_add=True)),
                ('people_start', models.CharField(max_length=50)),
                ('people_end', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='distribute',
            name='topic',
            field=models.ForeignKey(to='myapps.Topic'),
        ),
    ]
