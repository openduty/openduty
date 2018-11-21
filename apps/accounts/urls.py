__author__ = 'catalincoroeanu'

from django.conf.urls import url
from rest_framework import routers as rest_routers
from apps.accounts import views


rest_router = rest_routers.SimpleRouter(trailing_slash=False)
rest_router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'^$', views.list, name='openduty.users.list'),
    url(r'^new$', views.new, name='openduty.users.new'),
    url(r'^save', views.save, name='openduty.users.save'),
    url(r'^testnotification', views.testnotification, name='openduty.users.testnotification'),
    url(r'^edit/(\d+)$', views.edit, name='openduty.users.edit'),
    url(r'^delete/(\d+)$', views.delete),
]
