from celery import Celery
from modules import crawler 
from modules.db import pgTestClass as ptc
app = Celery('async_runner')
app.config_from_object('celeryConfig')

@app.task
def runSth():
    print('run something in flask !')
@app.task
def add(a,b):
    return a+b
# 定期爬youbike各站資料
@app.task
def runCrawler():
    print('begin to run crawler')
    dataSet = crawler.showAll()
    print('get ubike data')
    crawler.putData(dataSet)
    print('insert complete')

# 計算使用率並顯示於flask
@app.task
def runAnalyse(sno,sdate):
    run = ptc.DataConnection()
    print('begin to run analyzer')
    dtime,avg_sbi = run.avg_use_rate(sno,sdate)
    print('done')
    return dtime,avg_sbi