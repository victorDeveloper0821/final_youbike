from flask import Flask,render_template
from modules import crawler
app = Flask(__name__)
@app.route('/')
def home():
    return 'Home Page'
@app.route('/visual/<sno>',methods=['GET'])
def showData(sno):
    return render_template('visualData.html')
@app.route('/api/data/<sno>',methods=['GET'])
def showjson(sno):
    sno = str(sno)
    data = crawler.showStation(sno)
    return render_template('Station.html',ubike=data,station_number=sno)
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)