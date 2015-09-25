# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_booking_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='title',
        ),
    ]
