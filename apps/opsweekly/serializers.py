

from rest_framework import serializers


class NoneSerializer(serializers.Serializer):
    class Meta:
        fields = ()


class OpsWeeklySerializer(serializers.Serializer):
    occurred_at = serializers.DateTimeField()
    output = serializers.CharField(max_length=2000)
    incindent_key = serializers.CharField(max_length=200)


class OnCallSerializer(serializers.Serializer):
    person = serializers.CharField()
    email = serializers.EmailField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

