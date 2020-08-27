from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UserConfig(AppConfig):
    name = 'user'
    verbose_name = _('사용자')

    def ready(self):
        import user.signals
