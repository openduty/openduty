

from rest_framework import serializers


class NoneSerializer(serializers.Serializer):
    class Meta:
        fields = ()
