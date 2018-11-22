from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'id',
        'retry',
        'policy',
        'escalate_after',
        'notifications_disabled',
        'send_resolve_enabled',
    )
    list_filter = (
        'policy',
        'notifications_disabled',
        'send_resolve_enabled',
    )
    search_fields = ('name',)


class ServiceTokensAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'service_id', 'token_id')
    list_filter = ('service_id', 'token_id')
    search_fields = ('name',)


class ServiceSilencedAdmin(admin.ModelAdmin):

    list_display = ('id', 'service', 'silenced', 'silenced_until')
    list_filter = ('service', 'silenced', 'silenced_until')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Service, ServiceAdmin)
_register(models.ServiceTokens, ServiceTokensAdmin)
_register(models.ServiceSilenced, ServiceSilencedAdmin)
