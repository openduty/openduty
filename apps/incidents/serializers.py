from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.incidents.models import Incident


class IncidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incident
        fields = ('incident_key', 'service_key', 'event_type', 'description', 'details')
