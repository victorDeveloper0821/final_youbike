from celery import Celery
from modules import crawler 
app = Celery('async_runner')
app.config_from_object('celeryConfig')

@app.task
def runSth():
    print('run something in flask !')