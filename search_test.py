#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 10:51:12 2018

@author: dinohsu
"""
import psycopg2
secret = 'vqqpvcuodqrjrx:90416809f33bb59f2e09fcc604b90c31bfbe74148fb64848834c9cff647ead72'
secret = secret.split(':')
db_name = 'd9pmqffc3n91t'
db_host = 'ec2-54-243-210-70.compute-1.amazonaws.com'

conn = psycopg2.connect(dbname=db_name, user=secret[0], password=secret[1], host=db_host, port=5432)
cur = conn.cursor()




if __name__=='__main__':
    search_sno='station_0001'
    search_date='2018-06-05'
    ave_sbi=0
    ave_bemp=0
    
    print('搜尋站號:',search_sno)
    print('搜尋日期:',search_date)
    
    cur.execute("SELECT * FROM bike_station WHERE sno="+'\''+search_sno+'\''+" AND (MDATETIME::text LIKE '"+search_date+" 06:%:%' OR MDATETIME::text LIKE '"+search_date+" 07:%:%' OR MDATETIME::text LIKE '"+search_date+" 08:%:%' OR MDATETIME::text LIKE '"+search_date+" 09:%:%' OR MDATETIME::text LIKE '"+search_date+" 10:%:%' OR MDATETIME::text LIKE '"+search_date+" 11:%:%' OR MDATETIME::text LIKE '"+search_date+" 12:%:%');")
    rows = cur.fetchall()
    temp=0
    ave_sbi=0
    ave_bemp=0
    for row in rows:
        temp=temp+1
        ave_sbi=row[3]+ave_sbi
        ave_bemp=row[7]+ave_bemp
    ave_sbi=ave_sbi/temp    
    ave_bemp=ave_bemp/temp    
    print('早上sbi平均=',round(ave_sbi),';早上bemp平均=',round(ave_bemp))
    
    
    cur.execute("SELECT * FROM bike_station WHERE sno="+'\''+search_sno+'\''+" AND (MDATETIME::text LIKE '"+search_date+" 13:%:%' OR MDATETIME::text LIKE '"+search_date+" 14:%:%' OR MDATETIME::text LIKE '"+search_date+" 15:%:%' OR MDATETIME::text LIKE '"+search_date+" 16:%:%' OR MDATETIME::text LIKE '"+search_date+" 17:%:%' OR MDATETIME::text LIKE '"+search_date+" 18:%:%');")
    rows = cur.fetchall()
    temp=0
    ave_sbi=0
    ave_bemp=0
    for row in rows:
        temp=temp+1
        ave_sbi=row[3]+ave_sbi
        ave_bemp=row[7]+ave_bemp
    ave_sbi=ave_sbi/temp    
    ave_bemp=ave_bemp/temp    
    print('下午sbi平均=',round(ave_sbi),';下午bemp平均=',round(ave_bemp))
    
    cur.execute("SELECT * FROM bike_station WHERE sno="+'\''+search_sno+'\''+" AND (MDATETIME::text LIKE '"+search_date+" 19:%:%' OR MDATETIME::text LIKE '"+search_date+" 20:%:%' OR MDATETIME::text LIKE '"+search_date+" 21:%:%' OR MDATETIME::text LIKE '"+search_date+" 22:%:%' OR MDATETIME::text LIKE '"+search_date+" 23:%:%');")
    rows = cur.fetchall()
    temp=0
    ave_sbi=0
    ave_bemp=0
    for row in rows:
        temp=temp+1
        ave_sbi=row[3]+ave_sbi
        ave_bemp=row[7]+ave_bemp
    ave_sbi=ave_sbi/temp    
    ave_bemp=ave_bemp/temp    
    print('晚上上sbi平均=',round(ave_sbi),';晚上bemp平均=',round(ave_bemp))