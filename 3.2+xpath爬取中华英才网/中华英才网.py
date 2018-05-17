#conding:utf-8
from lxml import etree
import requests,random
from fake_useragent import UserAgent
agent=UserAgent()
url='http://www.chinahr.com/sou/?city=22%2C247%3B34%2C398%3B36%2C400%3B25%2C291%3B25%2C292&keyword=Python'
response=requests.get(url,headers={'User-Agent':agent.random})
# print(response)
root=etree.HTML(response.text)
# print(type(root))
a_list=root.xpath('//div[@class="jobList"]')
job=str()
for a in a_list:
    job_a=a.xpath('ul/li[@class="l1"]/span[@class="e1"]/a//text()')

    print(job_a)









    # for i in range(len(job_a)):
    #
    #     job=job_a[0]+job_a[i]
    #     print('---',job)
    # print(job_a)
    # job=job_a[0].split(',')
    # print(job)


    # if len(job_a)==1:
    #     job=job_a[0]
    #     print(job)
    # elif len(job_a)==2:
    #     job=job_a[0]+job_a[1]
    #     print(job)
    # else :
    #     job=job_a[0]+job_a[1]+job_a[2]
    #     print(job)
    # time_salary=a.xpath('ul/li/span[@class="e2"]/text()')
    # time=time_salary[0]
    # salary=time_salary[1]
    # address=a.xpath('ul/li[@class="l2"]/span[@class="e1"]/text()')
    # address = address[0].split('\r\n\t\t\t\t\t\t\t')[1].strip('[')
    # print(address)
    # print('发布日期',time)
    # print('薪资水平是：',salary)









    # print(job_a,len(job_a))
