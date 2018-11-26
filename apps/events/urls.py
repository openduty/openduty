from django.conf.urls import url
from apps.events import views



urlpatterns = [
    url(r'^create/(?P<calendar_slug>[-\w]+)/$', views.create_or_edit_event,
        name='openduty.events.create_or_edit_event'),
    # url(r'^create/(?P<calendar_slug>[-\w]+)/$', views.CreateUpdateEvent.as_view(),
    #     name='openduty.events.create_or_edit_event'),
    url(r'^edit/(?P<calendar_slug>[-\w]+)/(?P<event_id>\d+)/$', views.create_or_edit_event, name='edit_event'),
    url(r'^destroy/(?P<calendar_slug>[-\w]+)/(?P<event_id>\d+)/$', views.destroy_event, name='destroy_event'),
]
