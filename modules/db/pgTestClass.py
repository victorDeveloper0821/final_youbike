import psycopg2 as pg 
import os
from datetime import date,timedelta
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
    def insert_data(self,table,value):
        cmd = "INSERT INTO "+table+" (sno,name,total,sbi,district_id,mdatetime,act,bemp,addr) VALUES ("+",".join(value)+") ;"
        print(cmd)
        self.cursor.execute(cmd)
    def query_all(self,table,sno):
        cmd = "select * from "+table+" where sno="+'\''+sno+'\''+";"
        self.cursor.execute(cmd)
        rows = self.cursor.fetchall()
        return rows    
# 計算ubike平均使用率
    def avg_use_rate(self,search_sno,search_date):
        cmd_list = ["SELECT * FROM bike_station WHERE sno="+'\'station_'+search_sno+'\''+" AND (MDATETIME::text LIKE '"+search_date\
        +" 06:%:%' OR MDATETIME::text LIKE '"+search_date+" 07:%:%' OR MDATETIME::text LIKE '"+search_date+" 08:%:%' OR MDATETIME::text LIKE '"+\
        search_date+" 09:%:%' OR MDATETIME::text LIKE '"+search_date+" 10:%:%' OR MDATETIME::text LIKE '"+search_date+" 11:%:%' OR MDATETIME::text LIKE '"+\
        search_date+" 12:%:%');","SELECT * FROM bike_station WHERE sno="+'\'station_'+search_sno+'\''+" AND (MDATETIME::text LIKE '"+search_date+\
        " 13:%:%' OR MDATETIME::text LIKE '"+search_date+" 14:%:%' OR MDATETIME::text LIKE '"+search_date+" 15:%:%' OR MDATETIME::text LIKE '"+search_date+\
        " 16:%:%' OR MDATETIME::text LIKE '"+search_date+" 17:%:%' OR MDATETIME::text LIKE '"+search_date+" 18:%:%');","SELECT * FROM bike_station WHERE sno="+'\'station_'+search_sno\
        +'\''+" AND (MDATETIME::text LIKE '"+search_date+" 19:%:%' OR MDATETIME::text LIKE '"+search_date+" 20:%:%' OR MDATETIME::text LIKE '"+search_date+" 21:%:%' OR MDATETIME::text LIKE '"\
        +search_date+" 22:%:%' OR MDATETIME::text LIKE '"+search_date+" 23:%:%');"]
        period = ['早上','中午','下午']
        sbi_list = []
        index = 0
        for cmd in cmd_list:
            rows = self.cursor.execute(cmd)
            rows = self.cursor.fetchall()
            temp = 0
            ave_sbi = 0
            if rows == None:
                ave_sbi=0
                sbi_list.append(ave_sbi)
            else:
                for row in rows:
                    temp=temp+1
                    ave_sbi=row[3]+ave_sbi
                if temp==0:
                    ave_sbi=0
                else:
                    ave_sbi=ave_sbi/temp
                sbi_list.append(ave_sbi)
            period[index]=search_date+period[index]
            index+=1
        self.cursor.close()
        self.conn.close()
        return period,sbi_list

if __name__ == '__main__' : 
    Connection = DataConnection()
    print('setup database : testing')
    a,b = Connection.avg_use_rate('0368','2018-06-05')
    print(a)
    print(b)