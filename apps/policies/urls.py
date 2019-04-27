from django.urls import path
from apps.policies.views import (
    SchedulePolicyListView, SchedulePolicyDeleteView,
    SchedulePolicyCreateView, SchedulePolicyUpdateView
)


urlpatterns = [
    path('', SchedulePolicyListView.as_view(), name='SchedulePolicyListView'),
    path('new/', SchedulePolicyCreateView.as_view(), name='SchedulePolicyCreateView'),
    path('edit/<int:pk>/', SchedulePolicyUpdateView.as_view(), name="SchedulePolicyUpdateView"),
    path('delete/<int:pk>/', SchedulePolicyDeleteView.as_view(), name="openduty.escalation.delete"),
]
