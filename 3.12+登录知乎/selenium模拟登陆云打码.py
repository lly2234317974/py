#conding:utf-8
from YDMHTTP import YDMHttp
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

url='http://www.yundama.com'

driver=webdriver.Firefox()
driver.get(url)
username=WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id('username'))
username.send_keys('lly2234317974')
password=WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id('password'))
password.send_keys('123456789')
captcha=WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('verifyImg'))
captcha.screenshot(filename='captcha.png')
ydm=YDMHttp()
ydm.login()
cid,result=ydm.decode('captcha.png',5000,20)
# result=input('')
print(result)
driver.find_element_by_id('vcode').send_keys(result)
driver.find_element_by_class_name('sub').click()
import time
time.sleep(2)
