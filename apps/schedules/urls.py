from django.conf.urls import url
from django.urls import path
from schedule.periods import Month
from apps.schedules import views
from apps.schedules.views import SchedulesListView, SchedulesDetailView


urlpatterns = [
    path('', SchedulesListView.as_view(), name='SchedulesListView'), # name='SchedulesListView'
    url(r'^new$', views.new, name='openduty.schedules.new'),
    url(r'^save', views.save, name='openduty.schedules.save'),
    url(r'^edit/(?P<calendar_slug>[-\w]+)/$', views.edit, name='openduty.schedules.edit'),
    url(r'^delete/(?P<calendar_slug>[-\w]+)/$', views.delete, name='openduty.schedules.delete'),
    path('view/<slug:calendar_slug>/', SchedulesDetailView.as_view(),
         name='calendar_details', kwargs={'periods': [Month]}),
]
