from celery import shared_task
from game_indicators.indicator.models import Indicators


@shared_task
def reset_indicators():
    indicators = Indicators.objects.all()
    for indicator in indicators:
        indicator.values = 0
        indicator.save()