#!/usr/bin/env bash
corn --worker-class eventlet -w 1 wsgi
celery worker -l INFO -A flask-celery.celery
