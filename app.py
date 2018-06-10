from flask import Flask,render_template,url_for
from modules import crawler
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
    res = runAnalyse.delay(sno)
    date_list,avg_list = res.get()
    sname = crawler.showSingleVal(sno,'sna')
    addr = crawler.showSingleVal(sno,'ar')
    print(date_list,avg_list)
    return render_template('visualData.html',sname=sname,addr=addr,values=avg_list,dt = date_list)
@app.route('/api/data/<sno>',methods=['GET'])
def showjson(sno):
    sno = str(sno)
    data = crawler.showStation(sno)
    return render_template('Station.html',ubike=data,station_number=sno)
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)