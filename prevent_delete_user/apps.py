"""
App configuration for prevent_delete_user.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class EdxCustomizeUserConfig(AppConfig):
    """
    Customize User Plugin configuration.
    """
    name = 'prevent_delete_user'
    verbose_name = 'Customize User Plugin'

    plugin_app = {
        'url_config': {},
        'settings_config': {},
    }
