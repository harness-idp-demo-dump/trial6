from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "trial6.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import trial6.users.signals  # noqa: F401
        except ImportError:
            pass
