web: gunicorn app:app --timeout 100
worker: celery worker --app=celeryTask.app
beat: celery worker -A celeryTask.app --beat
