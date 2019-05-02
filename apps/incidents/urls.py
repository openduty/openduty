from django.conf.urls import url
from django.urls import path
from apps.incidents import views
from apps.incidents.views import IncidentDetailView, OnCallIncidentsListView, IncidentsListView


urlpatterns = [
    path('details/<int:pk>/', IncidentDetailView.as_view(), name='incident_details'),
    url(r'^update_type/$', views.update_type, name='openduty.incidents.update_type'),
    url(r'^forward_incident', views.forward_incident, name='openduty.incidents.forward_incident'),
    url(r'^silence/(.*)$', views.silence, name='openduty.incidents.silence'),
    url(r'^unsilence/(.*)$', views.unsilence, name='openduty.incidents.unsilence'),
    url(r'^on-call/$', OnCallIncidentsListView.as_view(), name="incidents_on_call"),
    url(r'^list/$', IncidentsListView.as_view(), name="incident_list")
]
