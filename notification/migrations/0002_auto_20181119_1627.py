# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('openduty', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulednotification',
            name='incident',
            field=models.ForeignKey(default=None, blank=True, to='openduty.Incident', null=True),
        ),
        migrations.AddField(
            model_name='schedulednotification',
            name='user_to_notify',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
