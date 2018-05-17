#conding:utf-8
import requests,json
url='http://api.map.baidu.com/telematics/v3/weather?&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'

name=input('请输入城市：')

response=requests.get(
    url=url,
    params={
        'location':name
    })
result=response.text.replace("'",'"')
# print(result)
json_list=json.loads(result)
# print(json_list)
city_list=json_list['results']
city_dict=city_list[0]
print('当前城市是：',city_dict['currentCity'])
weather_data=city_dict['weather_data']
for a in weather_data:

    print(a.get('date'))
    print(a.get('weather'))
    print(a.get('wind'))
    print(a.get('temperature'))
    print('\n')


    with open('weather.txt','a',encoding='utf-8') as f:
        f.write(a.get('date'))
        f.write(a.get('weather'))
        f.write(a.get('wind'))
        f.write(a.get('temperature'))
        f.write('\n')


# print(city_list)
# print(weather)