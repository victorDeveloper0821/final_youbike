from modules.db import pgTestClass as pgdb

def preload(dist):
    x = pgdb()
    print('load district data')
    x.preload_data(dist)
    x.conn.commit()
    x.cursor.close()
    print('close database')
    x.conn.close()

def truncate():
    x = pgdb()
    print('truncate data')
    x.truncate_data()
    x.conn.commit()
    x.cursor.close()
    print('close database')
    x.conn.close()
def dictToList(data):
    dset = list()
    for k,v in data.items():
        dset.append(('\''+'post_'+str(v)+'\'','\''+str(k)+'\''))
    return dset
if __name__=='__main__':
    data = {    
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
    }
    dist = dictToList(data)
    preload(dist)
    truncate()