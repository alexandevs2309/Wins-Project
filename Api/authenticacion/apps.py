from django.apps import AppConfig


class AuthenticacionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authenticacion'

    def ready(self):
        import authenticacion.signals