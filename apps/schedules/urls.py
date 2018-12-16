from django.conf.urls import url
from schedule.periods import Month
from apps.schedules import views


urlpatterns = [
    url(r'^$', views.list, name='schedules_list'),
    url(r'^new$', views.new, name='openduty.schedules.new'),
    url(r'^save', views.save, name='openduty.schedules.save'),
    url(r'^edit/(?P<calendar_slug>[-\w]+)/$', views.edit, name='openduty.schedules.edit'),
    url(r'^delete/(?P<calendar_slug>[-\w]+)/$', views.delete, name='openduty.schedules.delete'),
    url(r'^view/(?P<calendar_slug>[-\w]+)/$', views.details,
        name='calendar_details', kwargs={'periods': [Month]}),
]
