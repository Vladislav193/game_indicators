import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "game_indicators.settings")

app = Celery("game_indicators")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()