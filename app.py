from flask import Flask,render_template
from modules import crawler
from datetime import datetime,timedelta
from celeryTask import runSth,runAnalyse
app = Flask(__name__)

@app.before_request
def run():
    runSth.delay()
@app.route('/')
def home():
    return 'Home Page'
@app.route('/visual/<sno>',methods=['GET'])
def showData(sno):
    countDown = 4
    date_list = []
    avg_list = []
    while countDown>1:
        d = datetime.now().date()-timedelta(days=countDown)
        x = d.strftime('%Y-%m-%d')
        res = runAnalyse.delay(sno,x)
        dtime,avg = res.get()
        date_list = date_list+dtime
        avg_list = avg_list+avg
        countDown = countDown-1
#    d = '2018-06-05'
    sname = crawler.showSingleVal(sno,'sna')
    addr = crawler.showSingleVal(sno,'ar')
    print(date_list,avg_list)
    return render_template('visualData.html',sname=sname,addr=addr,values=avg_list)
@app.route('/api/data/<sno>',methods=['GET'])
def showjson(sno):
    sno = str(sno)
    data = crawler.showStation(sno)
    return render_template('Station.html',ubike=data,station_number=sno)
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)