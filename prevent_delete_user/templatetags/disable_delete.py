from django import template
from django.conf import settings
from django.contrib.auth.models import User

register = template.Library()


@register.simple_tag()
def disable_delete(original):
    if isinstance(original, User) and settings.FEATURES.get('PREVENT_DELETING_USER'):
        return True
    return False
