
import requests,json
#启动爬虫
response=requests.post(
url='http://localhost:6800/schedule.json',
data=
{'project':'项目名称'，
 ‘spider’：‘爬虫名字’}
)
关闭爬虫
json_rea=response.json()
jobid=json_rea['jobid']
req=requests.post(
url='http://localhost:6800/cancel.json',
data={
'project':'项目名称'},
'job':jobid)