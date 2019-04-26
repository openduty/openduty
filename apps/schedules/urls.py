from django.urls import path
from apps.schedules.views import (
    SchedulesListView, SchedulesDetailView, SchedulesDeleteView, SchedulesCreateView, SchedulesUpdateView
)


urlpatterns = [
    path('', SchedulesListView.as_view(), name='SchedulesListView'),
    path('new/', SchedulesCreateView.as_view(), name='SchedulesCreateView'),
    path('edit/<slug:calendar_slug>/', SchedulesUpdateView.as_view(), name="SchedulesUpdateView"),
    path('delete/<slug:calendar_slug>/', SchedulesDeleteView.as_view(), name="SchedulesDeleteView"),
    path('view/<slug:calendar_slug>/', SchedulesDetailView.as_view(), name='calendar_details'),
]
