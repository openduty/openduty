__author__ = 'catalincoroeanu'

from django.conf.urls import url
from apps.services import views


urlpatterns = [
    url(r'^token_delete/(.*)$', views.token_delete),
    url(r'^token_create/(.*)$', views.token_create),
]
