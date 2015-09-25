# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
        ('bookings', '0005_remove_booking_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='talent',
        ),
        migrations.AddField(
            model_name='booking',
            name='resource',
            field=models.ForeignKey(related_name='bookings', default=1, to='resources.Resource'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='project',
            field=models.ForeignKey(related_name='bookings', to='projects.Project'),
        ),
    ]
