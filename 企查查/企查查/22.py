#coding:utf-8
import re
a=([{"t":"13701631662","s":"2017"},{"t":"13918126104","s":"2016"}],"13701631662")

a1=a[1]
print(a1)
list1=a[0]
list_all=[]
list_all.append(a1)
for z in list1:
    phone=z['t']
    print('扣扣发个颇多',phone)
    pattern = re.compile(r"^1([358][0-9]|4[579]|66|7[0135678]|9[89])[0-9]{8}$")
    result=pattern.match(phone)
    # print(result)
    if result != 'None':
        if phone not in list_all:
            list_all.append(phone)
            print(list_all)
print(list_all
)
d=len(list_all)
print(d)
if d==0 :
    phone1=0
    phone2=0
    phone3=0
    phone4=0
if d == 1:
    phone1=list_all[0]
    phone2 = 0
    phone3 = 0
    phone4 = 0
if d== 2:
    phone1=list_all[0]
    phone2=list_all[1]
    phone3=''
    phone4=''
    print(phone1,phone2,phone3,phone4)
if d == 3:
    phone1=list_all[0]
    phone2=list_all[1]
    phone3=list_all[2]
    phone4=0
if d==4:
    phone1 = list_all[0]
    phone2 = list_all[1]
    phone3 = list_all[2]
    phone4 = list_all[3]



