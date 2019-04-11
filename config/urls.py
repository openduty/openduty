from django.conf import settings
from django.conf.urls import url
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers as rest_routers
from rest_framework.authtoken.views import obtain_auth_token
from apps.accounts.views import do, logout, UserViewSet, GroupViewSet, UserLoginView
from apps.policies.views import SchedulePolicyViewSet, SchedulePolicyRuleViewSet
from apps.incidents.views import IncidentViewSet
from apps.openduty.views import HealthCheckViewSet, CeleryHealthCheckViewSet
from apps.openduty import call_handler, event_log
from apps.opsweekly.views import OpsWeeklyIncidentViewSet, OpsWeeklyOnCallViewSet


admin.autodiscover()
rest_router = rest_routers.SimpleRouter(trailing_slash=False)
rest_router.register(r'users', UserViewSet)
rest_router.register(r'groups', GroupViewSet)
rest_router.register(r'schedule_policies', SchedulePolicyViewSet)
rest_router.register(r'schedule_policy_rules', SchedulePolicyRuleViewSet)
rest_router.register(r'create_event', IncidentViewSet)
rest_router.register(r'incident', IncidentViewSet)
rest_router.register(r'healthcheck', HealthCheckViewSet)
rest_router.register(r'celeryhealthcheck', CeleryHealthCheckViewSet)
rest_router.register(r'opsweekly', OpsWeeklyIncidentViewSet)
rest_router.register(r'oncall', OpsWeeklyOnCallViewSet)

urlpatterns = [
    path('', event_log.list),
    path('dashboard/', event_log.list, name='dashboard'),
    url(r'^dashboard/service/(.*)', event_log.get, name='event_log_detail'),
    path('api-token-auth/', obtain_auth_token),
    path('login/', UserLoginView.as_view(), name='login'),
    path('login/do/', do, name='openduty.auth.do'),
    path('logout/', logout, name='logout'),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(rest_router.urls)),

    path('users/', include('apps.accounts.urls')),
    path('services/', include('apps.services.urls')),
    path('policies/', include('apps.policies.urls')),
    path('schedule/', include('schedule.urls')),
    path('schedules/', include('apps.schedules.urls')),
    path('events/', include('apps.events.urls')),
    path('services/', include('apps.services.urls')),
    path('incidents/', include('apps.incidents.urls')),

    path('twilio/(\d+)/(\d+)', call_handler.read_notification),
    path('twilio/handle/(\d+)/(\d+)', call_handler.handle_key),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]



