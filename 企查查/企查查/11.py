
import re
list=[]
f2 = open("C:/Users/Administrator/Desktop/1.txt","r")
lines = f2.readlines()
for line3 in lines:
    line3=re.sub('\n','',line3)
    list.append(line3)

for x in list:
    url='<table><img src="http://t.ashiyue.com/img/barcodegen/html/image.php?filetype=PNG&dpi=72&scale=2&rotation=0&font_family=Arial.ttf&font_size=14&text={}&thickness=20&start=NULL&code=BCGcode128"/>'.format(x)
    print(url)