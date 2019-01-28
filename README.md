# final_youbike
- 用台北市youbike open data創造更好的生活
---
## 功能:
- 即時youbike站點空位查詢
- 計算近三天早上,中午及晚上youbike的使用率
- 站點依照區域進行使用率排名
## 使用library:
- Flask
- PostgresQL **之後會考慮使用MongoDB儲存row data**
- Celery **用於執行異步的爬蟲程式**

## 系統改進
- 資料儲存方式改用redis,以增加系統效能
- 新增Kafka架構以存取多種open data
