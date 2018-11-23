import hmac
import uuid
from hashlib import sha1
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(max_length=40, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        unique = uuid.uuid4()
        return hmac.new(unique.bytes, digestmod=sha1).hexdigest()

    def __unicode__(self):
        return self.key

    def __str__(self):
        return self.key


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    pushover_user_key = models.CharField(max_length=50)
    pushover_app_key = models.CharField(max_length=50)
    slack_room_name = models.CharField(max_length=50)
    prowl_api_key = models.CharField(max_length=50, blank=True)
    prowl_application = models.CharField(max_length=256, blank=True)
    prowl_url = models.CharField(max_length=512, blank=True)
    rocket_webhook_url = models.CharField(max_length=512, blank=True)
    hipchat_room_name = models.CharField(max_length=100)
    hipchat_room_url = models.CharField(max_length=100)
    send_resolve_enabled = models.BooleanField(default=False)
