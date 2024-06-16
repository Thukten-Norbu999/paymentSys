from django.apps import AppConfig


class UseraccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'useraccount'

class AccountConfig(AppConfig):

    name = 'useraccount'

    def ready(self) -> None:
        import useraccount.signals

        