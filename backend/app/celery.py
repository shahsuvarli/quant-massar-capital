from celery import Celery
from celery.schedules import crontab

app.conf.beat_schedule = {
    'update-risk-metrics-every-day': {
        'task': 'risk.tasks.update_risk_metrics',
        'schedule': crontab(hour=0, minute=0),  # Runs at midnight
    },
}


app = Celery("quant-massar")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
