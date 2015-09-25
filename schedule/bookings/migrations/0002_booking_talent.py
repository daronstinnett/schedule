# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='talent',
            field=models.ForeignKey(default=1, to='talent.Talent'),
            preserve_default=False,
        ),
    ]
