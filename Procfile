web: gunicorn app:app 
worker: celery worker --app=celeryTask.app
beat: celery worker --app=celeryTask.app beat
