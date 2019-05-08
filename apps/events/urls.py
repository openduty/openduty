from django.urls import path
from apps.events.views import CustomCreateEventView, CustomUpdateEventView, CustomDeleteEventView


urlpatterns = [
    path('create/<slug:calendar_slug>/', CustomCreateEventView.as_view(), name='CustomCreateEventView'),
    path('edit/<slug:calendar_slug>/<int:event_id>/', CustomUpdateEventView.as_view(), name='edit_event'),
    path('destroy/<slug:calendar_slug>/<int:event_id>/', CustomDeleteEventView.as_view(), name='destroy_event'),
]
