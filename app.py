from flask import Flask,render_template,url_for
from modules import crawler
from modules.db import pgTestClass as ptc
from datetime import datetime,timedelta
from celeryTask import runSth,runAnalyse
app = Flask(__name__)

@app.before_request
def run():
    runSth.delay()
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/visual/<sno>',methods=['GET'])
def showData(sno):
"""
    res = runAnalyse.delay(sno)
    date_list,avg_list = res.get()
    sname = crawler.showSingleVal(sno,'sna')
    addr = crawler.showSingleVal(sno,'ar')
    print(date_list,avg_list)
"""
    sname = crawler.showSingleVal(sno,'sna')
    addr = crawler.showSingleVal(sno,'ar')
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
    run.cursor.close()
    run.conn.close()
    return render_template('visualData.html',sname=sname,addr=addr,values=avg_list,dt = date_list)
@app.route('/api/data/<sno>',methods=['GET'])
def showjson(sno):
    sno = str(sno)
    data = crawler.showStation(sno)
    return render_template('Station.html',ubike=data,station_number=sno)
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)