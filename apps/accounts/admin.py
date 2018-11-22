from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class TokenAdmin(admin.ModelAdmin):

    list_display = ('key', 'created')
    list_filter = ('created',)


class UserProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'phone_number',
        'pushover_user_key',
        'pushover_app_key',
        'slack_room_name',
        'prowl_api_key',
        'prowl_application',
        'prowl_url',
        'rocket_webhook_url',
        'hipchat_room_name',
        'hipchat_room_url',
        'send_resolve_enabled',
    )
    list_filter = ('user', 'send_resolve_enabled')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Token, TokenAdmin)
_register(models.UserProfile, UserProfileAdmin)
