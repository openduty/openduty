from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class SchedulePolicyAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'repeat_times')
    search_fields = ('name',)


class SchedulePolicyRuleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'schedule_policy',
        'position',
        'user_id',
        'group_id',
        'schedule',
        'escalate_after',
    )
    list_filter = ('schedule_policy', 'user_id', 'group_id', 'schedule')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.SchedulePolicy, SchedulePolicyAdmin)
_register(models.SchedulePolicyRule, SchedulePolicyRuleAdmin)
