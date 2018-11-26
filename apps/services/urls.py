from django.conf.urls import url
from apps.services import views


urlpatterns = [
    url(r'^$', views.list, name='openduty.services.list'),
    url(r'^token_delete/(.*)$', views.token_delete, name='openduty.services.token_delete'),
    url(r'^token_create/(.*)$', views.token_create, name='openduty.services.token_create'),
    url(r'^new$', views.new, name='openduty.services.new'),
    url(r'^save', views.save, name='openduty.services.save'),
    url(r'^edit/(.*)$', views.edit, name="openduty.services.edit"),
    url(r'^delete/(.*)$', views.delete, name='openduty.services.delete'),
    url(r'^silence/(.*)$', views.silence, name='openduty.services.silence'),
    url(r'^unsilence/(.*)$', views.unsilence, name='openduty.services.unsilence'),
]
