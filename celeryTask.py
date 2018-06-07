from celery import Celery
from modules import crawler 
from modules.db import pgTestClass
app = Celery('async_runner')
app.config_from_object('celeryConfig')

@app.task
def runSth():
    print('run something in flask !')
@app.task
def add(a,b):
    return a+b
@app.task
def runCrawler():
    print('begin to run crawler')
    dataSet = crawler.showAll()
    print('get ubike data')
    crawler.putData(dataSet)
    print('insert complete')
@app.task
def runAnalyse(sno,sdate):
    run = pgTestClass()
    print('begin to run analyzer')
    dtime,avg_sbi = run.avg_use_rate(sno,sdate)
    print('done')
    return dtime,avg_sbi