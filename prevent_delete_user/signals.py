import logging
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_delete
log = logging.getLogger(__name__)


@receiver(pre_delete, sender=User)
def prevent_delete_user(sender, instance, **kwargs):
    if settings.FEATURES.get('PREVENT_DELETING_USER'):
        log.error("Not permission to delete user {}".format(instance.username), exc_info=True)
        raise PermissionDenied()
