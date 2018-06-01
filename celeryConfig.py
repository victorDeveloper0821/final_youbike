import os 
broker_url= os.environ.get('REDIS_URL',None)
result_backend= os.environ.get('DATABASE_URL',None)
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Taipei'
enable_utc = True