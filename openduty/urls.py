from django.conf import settings
from django.conf.urls import url
from rest_framework import routers as rest_routers
from django.urls import path, include
from django.conf.urls.static import static
from openduty import views
from django.contrib import admin
from schedule.periods import Month
from .models import Incident
from .tables import IncidentTable
from django_tables2_simplefilter import FilteredSingleTableView
from rest_framework.authtoken.views import obtain_auth_token
from openduty import (auth, users, services, escalation, schedules, events, event_log,
                      incidents, call_handler, healthcheck, opsweekly)


admin.autodiscover()
rest_router = rest_routers.SimpleRouter(trailing_slash=False)
rest_router.register(r'users', views.UserViewSet)
rest_router.register(r'groups', views.GroupViewSet)
rest_router.register(r'schedule_policies', views.SchedulePolicyViewSet)
rest_router.register(r'schedule_policy_rules', views.SchedulePolicyRuleViewSet)
rest_router.register(r'create_event', incidents.IncidentViewSet)
rest_router.register(r'incident', incidents.IncidentViewSet)
rest_router.register(r'healthcheck', healthcheck.HealthCheckViewSet)
rest_router.register(r'celeryhealthcheck', healthcheck.CeleryHealthCheckViewSet)
rest_router.register(r'opsweekly', opsweekly.OpsWeeklyIncidentViewSet)
rest_router.register(r'oncall', opsweekly.OpsWeeklyOnCallViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^api/', include(rest_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_auth_token),
    path('admin/', admin.site.urls),
    url(r'^schedule/', include('schedule.urls')),

    #AUTH
    path('login/', auth.login, name='openduty.auth.login'),
    url(r'^login/do$', auth.do, name='openduty.auth.do'),
    url(r'^logout/$', auth.logout, name='openduty.auth.logout'),

    #USERS
    url(r'^users/$', users.list, name='openduty.users.list'),
    url(r'^users/new$', users.new, name='openduty.users.new'),
    url(r'^users/save', users.save, name='openduty.users.save'),
    url(r'^users/testnotification', users.testnotification, name='openduty.users.testnotification'),
    url(r'^users/edit/(\d+)$', users.edit, name='openduty.users.edit'),
    url(r'^users/delete/(\d+)$', users.delete),

    #SERVICES
    url(r'^services/$', services.list, name='openduty.services.list'),
    url(r'^services/new$', services.new, name='openduty.services.new'),
    url(r'^services/save', services.save, name='openduty.services.save'),
    url(r'^services/edit/(.*)$', services.edit, name="service_detail"),
    url(r'^services/delete/(.*)$', services.delete, name='openduty.services.delete'),
    url(r'^services/silence/(.*)$', services.silence, name='openduty.services.silence'),
    url(r'^services/unsilence/(.*)$', services.unsilence, name='openduty.services.unsilence'),

    #Policies
    url(r'^policies/$', escalation.list, name='openduty.escalation.list'),
    url(r'^policies/new$', escalation.new, name='openduty.escalation.new'),
    url(r'^policies/save', escalation.save, name='openduty.escalation.save'),
    url(r'^policies/edit/(.*)$', escalation.edit, name='openduty.escalation.edit'),
    url(r'^policies/delete/(.*)$', escalation.delete, name='openduty.escalation.delete'),


    #SCHEDULES
    url(r'^schedules/$', schedules.list, name='openduty.schedules.list'),
    url(r'^schedules/new$', schedules.new, name='openduty.schedules.new'),
    url(r'^schedules/save', schedules.save, name='openduty.schedules.save'),
    url(r'^schedules/edit/(?P<calendar_slug>[-\w]+)/$', schedules.edit, name='openduty.schedules.edit'),
    url(r'^schedules/delete/(?P<calendar_slug>[-\w]+)/$', schedules.delete, name='openduty.schedules.delete'),
    url(r'^schedules/view/(?P<calendar_slug>[-\w]+)/$', schedules.details,
        name='calendar_details',  kwargs={'periods': [Month]}),

    #EVENT
    url(r'^events/create/(?P<calendar_slug>[-\w]+)/$', events.create_or_edit_event, name='openduty.events.create_or_edit_event'),
    url(r'^events/edit/(?P<calendar_slug>[-\w]+)/(?P<event_id>\d+)/$', events.create_or_edit_event, name='edit_event'),
    url(r'^events/destroy/(?P<calendar_slug>[-\w]+)/(?P<event_id>\d+)/$', events.destroy_event, name='destroy_event'),



    #SERVICES/API TOKEN
    url(r'^services/token_delete/(.*)$', services.token_delete),
    url(r'^services/token_create/(.*)$', services.token_create),

    #EVENT_LOG
    url(r'^$', event_log.list),
    url(r'^dashboard/$', event_log.list, name='openduty.event_log.list'),
    url(r'^dashboard/service/(.*)$', event_log.get),

    #INCIDENTS
    url(r'^incidents/details/(.*)$', incidents.details, name='openduty.incidents.details'),
    url(r'^incidents/update_type/$', incidents.update_type, name='openduty.incidents.update_type'),
    url(r'^incidents/forward_incident', incidents.forward_incident, name='openduty.incidents.forward_incident'),
    url(r'^incidents/silence/(.*)$', incidents.silence, name='openduty.incidents.silence'),
    url(r'^incidents/unsilence/(.*)$', incidents.unsilence, name='openduty.incidents.unsilence'),
    url(r'^incidents/on-call/$', incidents.ServicesByMe.as_view(), name="incidents_on_call" ),
    url(r'^incidents/list/$',
        FilteredSingleTableView.as_view(template_name='incidents/list2.html',
                                        table_class=IncidentTable, model=Incident,
                                        table_pagination={"per_page": 10},
                                        ),
        name='incident_list'),
   url(r'^twilio/(\d+)/(\d+)$', call_handler.read_notification),
   url(r'^twilio/handle/(\d+)/(\d+)$', call_handler.handle_key),


]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]


