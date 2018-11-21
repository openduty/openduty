__author__ = 'deathowl'

from rest_framework import serializers
from apps.policies.models import SchedulePolicy, SchedulePolicyRule


class SchedulePolicySerializer(serializers.HyperlinkedModelSerializer):
    rules = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = SchedulePolicy
        fields = ('name', 'repeat_times', 'rules')


class SchedulePolicyRuleSerializer(serializers.HyperlinkedModelSerializer):
    rules = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = SchedulePolicyRule
        fields = ('schedule_policy', 'position', 'user_id', 'group_id', 'schedule', 'escalate_after')
