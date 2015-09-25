# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_booking_talent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='end_date',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='start_date',
            new_name='start',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='text',
        ),
        migrations.AddField(
            model_name='booking',
            name='title',
            field=models.CharField(default='title', max_length=63),
            preserve_default=False,
        ),
    ]
