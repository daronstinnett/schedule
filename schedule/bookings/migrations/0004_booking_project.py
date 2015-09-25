# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('bookings', '0003_auto_20150818_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='project',
            field=models.ForeignKey(default=2, to='projects.Project'),
            preserve_default=False,
        ),
    ]
