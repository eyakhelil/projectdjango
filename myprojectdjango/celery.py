from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

# Indiquer le settings de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myprojectdjango.settings')

app = Celery('myprojectdjango')
app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'

# Configurer à partir des settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover des tâches dans les apps Django
app.autodiscover_tasks()
