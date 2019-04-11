from django.conf.urls import url
from apps.accounts import views


urlpatterns = [
    url(r'^$', views.list, name='openduty.users.list'),
    url(r'^new$', views.new, name='add_user'),
    url(r'^save', views.save, name='openduty.users.save'),
    url(r'^testnotification', views.testnotification, name='openduty.users.testnotification'),
    url(r'^edit/(\d+)$', views.edit, name='edit_profile'),
    url(r'^delete/(\d+)$', views.delete, name='openduty.users.delete'),
]
