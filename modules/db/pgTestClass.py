import psycopg2 as pg 
import os

class DataConnection :
    def __init__(self) : 
        secret = str(os.environ.get('DB_secret',None))
        secret = secret.split(':')
        db_name = str(os.environ.get('DB_name',None))
        db_host = str(os.environ.get('DB_host',None))
        try : 
            self.conn = pg.connect(user=secret[0],password=secret[1],port=5432,dbname=db_name,host=db_host)
            self.cursor = self.conn.cursor()
            print('set up connection')
        except:
            print('connection error')
    def preload_data(self,data):
        if self.conn ==None : 
            print('connection = None')
            pass
        if data == None:
            print('data are not available')
            pass
        for d in data:
            cmd  = "insert into district values ("+",".join(d)+");"
            self.cursor.execute(cmd)
    def truncate_data(self,table='bike_station'):
        if self.conn ==None : 
            print('connection = None')
            pass
        cmd = "truncate table %s ;"%table
        self.cursor.execute(cmd)
    def insert_data(self,table,value):
        cmd = "INSERT INTO "+table+" (sno,name,total,sbi,district_id,mdatetime,act,bemp,addr) VALUES ("+",".join(value)+") ;"
        print(cmd)
        self.cursor.execute(cmd)
    def query_all(self,table,sno):
        cmd = "select * from "+table+" where sno="+'\''+sno+'\''+";"
        self.cursor.execute(cmd)
        rows = self.cursor.fetchall()
        return rows    
if __name__ == '__main__' : 
#    testdata = ('victor','pythontest12345',5400) # 0->user , 1->passwd , 2->port number
    Connection = DataConnection()
    print('setup database : testing')
    r = Connection.query_all('bike_station01','station_0001')
    print(r)