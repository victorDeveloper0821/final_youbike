from celery import Celery
from modules import crawler 
from modules.db import pgTestClass as ptc
app = Celery('async_runner')
app.config_from_object('celeryConfig')

@app.task(ignore_result=True)
def runSth():
    print('run something in flask !')
@app.task(ignore_result=True)
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
@app.task(ignore_result=True)
def runAnalyse(sno):
    countDown = 4
    date_list = []
    avg_list = []
    run = ptc.DataConnection()
    print('begin to run analyzer')
    while countDown>1:
        d = datetime.now().date()-timedelta(days=countDown)
        date = d.strftime('%Y-%m-%d')
        dtime,avg = run.avg_use_rate(sno,date)
        date_list = date_list+dtime
        avg_list = avg_list+avg
        countDown = countDown-1
    print('done')
    return date_list,avg_list