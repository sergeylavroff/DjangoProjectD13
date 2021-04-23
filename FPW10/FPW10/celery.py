import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FPW10.settings')

app = Celery('FPW10')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.schedule_notify_subscribers = {
    'news_notify_every_mon_8': {
        'task': 'news.tasks.schedule_notify_subscribers',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args': (),
    },
}