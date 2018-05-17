#conding:utf-8
import requests
response=requests.get('http://localhost:6800/daemonstatus.json')

result=response.json()
if result.get('status') =='ok':
    running=result.get('running')
    pending=result.get('pending')
    finished=result.get('finished')
    print('爬虫状态：OK，正在运行{}个爬虫，待定状态{}个爬虫，已经结束{}个爬虫'.format(running,pending,finished))
# response=requests.post(
#     url='http://localhost:6800/schedule.json',
#     data={
#         'project':'ZL',
#         'spider':'zl'
#     }
# )
# rs=response.json()
# if rs.get('status')=='ok':
#     jobid=rs.get('jobid')
#
# print(jobid)
response=requests.post(
    url='http://localhost:6800/cancel.json',
    data={
        'project':'ZL',
        'job':'afad628c2dcb11e8bef6005056c00008'
    }
)