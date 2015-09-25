# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20150820_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contract',
            field=models.ForeignKey(default=1, to='projects.Contract'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='notes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.ForeignKey(default=1, to='projects.Type'),
            preserve_default=False,
        ),
    ]
