from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


def _register(model, admin_class):
    admin.site.register(model, admin_class)


