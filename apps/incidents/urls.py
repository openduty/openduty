from django.urls import path
from apps.incidents.views import (
    IncidentDetailView, OnCallIncidentsListView, IncidentsListView,
    update_type, forward_incident, silence, unsilence
)


urlpatterns = [
    path('details/<int:pk>/', IncidentDetailView.as_view(), name='IncidentDetailView'),
    path('update_type/', update_type, name='incidents_update_type'),
    path('forward_incident/', forward_incident, name='incidents_forward_incident'),
    path('silence/<int:incident_id>/', silence, name='incidents_silence'),
    path('unsilence/<int:incident_id>/', unsilence, name='incidents_unsilence'),
    path('on-call/', OnCallIncidentsListView.as_view(), name="OnCallIncidentsListView"),
    path('list/', IncidentsListView.as_view(), name="IncidentsListView")
]
