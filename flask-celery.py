__author__ = 'nickyuan'
from TODOCalendar import app
from flask import Flask
from celery import Celery

# Only for those who run server on Linux
from celery import platforms

platforms.C_FORCE_ROOT = True


def make_celery(app):
    celery = Celery('flask-celery',
                    broker=app.config['CELERY_BROKER_URL'],
                    backend=app.config['CELERY_RESULT_BACKEND']
                    )
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    ContextTask = celery.Task
    return celery


app.config.update(
        CELERY_BROKER_URL='redis://localhost:6379/0',
        CELERY_RESULT_BACKEND='redis://localhost:6379/1'
)

celery = make_celery(app)


@celery.task
def celery_work():
    pass


@app.route('/')
def hello():
    result = celery_work.delay(10,20)
    #task = my_background_task.apply_async(args=[10, 20], countdown=60)
    return 'Done'
