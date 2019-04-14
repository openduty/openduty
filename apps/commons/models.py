import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampModel(models.Model):
    """
    Abstract TimeStamp Based Model to inherit from:
        - created
        - updated
    """
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=_('Created at'))
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    """
    Abstract Base Model to inherit from:
        - uuid
    """
    uuid = models.UUIDField(unique=True, db_index=True, default=uuid.uuid4, verbose_name=_('Unique ID'))

    class Meta:
        abstract = True


class BaseModel(models.Model):
    """
    Abstract Base Model to inherit from:
        - uuid
        - created
        - updated
    """
    uuid = models.UUIDField(unique=True, db_index=True, default=uuid.uuid4, verbose_name=_('Unique ID'))
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=_('Created at'))
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        abstract = True
