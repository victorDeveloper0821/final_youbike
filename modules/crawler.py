# -*- coding: utf-8 -*-
"""
Created on Thu May  3 12:12:44 2018

@author: victor
"""

import requests
import json
from io import StringIO
import datetime
from modules.db import pgTestClass

r = requests.get('http://data.taipei/youbike')
s = StringIO(r.text)
data = json.loads(r.text)

def showSingleVal(sno,key):
    if data['retCode'] != 1 :
        print('unexpect error')
        return None
    info = data['retVal'].get(sno)
    if key in info.keys():
        return info[key]
    else :
        print('key:%s dosent exist'%key)
        return None
def showStation(sno):
    d = dict()
    dt = datetime.datetime.now()+datetime.timedelta(hours=8)
    if data['retCode'] != 1 :
        print('unexpect error')
        return None
    info = data['retVal'].get(sno)
    
    if info == None :
        return None

    d['sno'] = info.get('sno')
    d['sna'] = info.get('sna')
    d['tot'] = info.get('tot')
    d['sbi'] = info.get('sbi')
    d['ar'] = info.get('ar')
    d['bemp'] = info.get('bemp')
    d['lng'] = info.get('lng')
    d['lat'] = info.get('lat')
    d['mday'] =dt.strftime("%Y-%m-%d %H:%M:%S")

    return d
def areaTocode(sname):
     return {
        '大安區': '106',
        '信義區': '110',
        '中正區':'100',
        '士林區':'111',
        '北投區':'112',
        '萬華區':'108',
        '內湖區':'114',
        '南港區':'115',
        '中山區':'104',
        '大同區':'103',
        '松山區':'105',
        '文山區':'116',
    }[sname]

#所有插入資料用list儲存     
def showAll():
    ubike_data = data['retVal'].values()
    dSet = tuple()
    empList = []
    for i in ubike_data:
        sid = '\''+'station_'+str(i['sno'])+'\''
        post_id = '\''+'post_'+areaTocode(i['sarea'])+'\''
        stampTime = '\''+datetime.datetime.now()+datetime.timedelta(hours=8).strftime("%Y-%m-%d %H:%M:%S")+'\''
        dSet = (sid,'\''+i['sna']+'\'',i['tot'],i['sbi'],post_id,stampTime,i['act'],i['bemp'],'\''+i['ar']+'\'')
#        print(dSet)
        empList.append(dSet)
    return empList

# 以tuple為單位放入資料
def putData(bike):
    a = pgTestClass.DataConnection()
    for tup in bike:
        a.insert_data('bike_station',tup)
    a.conn.commit()
    a.cursor.close()
    a.conn.close()
    print('data are inserted')

if __name__=='__main__':
# codes used for testing the functions .
# When the python file is excuted as a single script , the following codes are excuted .
    a = showAll()    
#    print(showStation('0310'))
    print(a)