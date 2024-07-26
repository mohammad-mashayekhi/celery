from celery import Celery
import os

os.environ.setdefault('DLANGO_SETTING_MODULE','config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.conf.beat_schedule = {
    'mytask_every_2sec':{
        'task':'home.tasks.mytask2',
        'schedule':2,
        'options':{
            'expires':10,
        }
    }
}