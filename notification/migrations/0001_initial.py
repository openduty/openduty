# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notifier', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=500)),
                ('send_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'openduty_schedulednotification',
                'verbose_name': 'scheduled_notifications',
                'verbose_name_plural': 'scheduled_notifications',
            },
        ),
        migrations.CreateModel(
            name='UserNotificationMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField()),
                ('method', models.CharField(max_length=50)),
                ('user', models.ForeignKey(related_name='notification_methods', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'openduty_usernotificationmethod',
                'verbose_name': 'user_notification_method',
                'verbose_name_plural': 'user_notification_methods',
            },
        ),
    ]
