__author__ = 'catalincoroeanu'

from django.conf.urls import url
from apps.policies import views


urlpatterns = [
    url(r'^$', views.list, name='openduty.escalation.list'),
    url(r'^new$', views.new, name='openduty.escalation.new'),
    url(r'^save', views.save, name='openduty.escalation.save'),
    url(r'^edit/(.*)$', views.edit, name='openduty.escalation.edit'),
    url(r'^delete/(.*)$', views.delete, name='openduty.escalation.delete'),
]
