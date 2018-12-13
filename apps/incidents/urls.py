from django.conf.urls import url
from django_tables2_simplefilter import FilteredSingleTableView
from apps.incidents.tables import IncidentTable
from apps.incidents.models import Incident
from apps.incidents import views


urlpatterns = [
    url(r'^details/(.*)$', views.details, name='incident_details'),
    url(r'^update_type/$', views.update_type, name='openduty.incidents.update_type'),
    url(r'^forward_incident', views.forward_incident, name='openduty.incidents.forward_incident'),
    url(r'^silence/(.*)$', views.silence, name='openduty.incidents.silence'),
    url(r'^unsilence/(.*)$', views.unsilence, name='openduty.incidents.unsilence'),
    url(r'^on-call/$', views.OnCallIncidentsListView.as_view(), name="incidents_on_call"),
    url(r'^list/$', views.IncidentsListView.as_view(), name="incident_list")
]
