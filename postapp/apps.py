from django.apps import AppConfig


class PostappConfig(AppConfig):
    name = 'postapp'

    def ready(self):
        import postapp.signals