# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class UserNotificationMethodAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'position', 'method')
    list_filter = ('user',)


class ScheduledNotificationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'notifier',
        'message',
        'user_to_notify',
        'send_at',
        'incident',
    )
    list_filter = ('user_to_notify', 'send_at', 'incident')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.UserNotificationMethod, UserNotificationMethodAdmin)
_register(models.ScheduledNotification, ScheduledNotificationAdmin)
