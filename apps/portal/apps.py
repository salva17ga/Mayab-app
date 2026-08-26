from django.apps import AppConfig


class PortalConfig(AppConfig):
    name = 'apps.portal'

    def ready(self):
        import apps.portal.signals
