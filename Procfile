web: gunicorn app:app 
worker: celery worker --app=celeryTask.app
beat: celery worker -A celeryTask.app --beat
