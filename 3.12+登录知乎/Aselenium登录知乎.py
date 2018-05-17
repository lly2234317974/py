#conding:utf-8
from YDMHTTP import YDMHttp
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from urllib import request
from lxml import etree
driver=webdriver.Chrome()
driver.get('https://www.zhihu.com/signup?next=%2F')
driver.find_element_by_xpath('//div[@class="SignContainer-switch"]/span').click()
username=WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_name('username'))
username.send_keys('15736959834')
password=WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_name('password'))
password.send_keys('199666lly')
res=driver.find_element_by_xpath('//div[contains(@class,"Captcha")]/img')

if res.get_attribute('src')==0:
    driver.find_element_by_xpath('//div[@class="Login-content"]/form/button').click()
else:
    if res.get_attribute('class')=='Captcha-englishImg':
        captcha = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_class_name('Captcha-englishImg'))
        captcha.screenshot(filename='captcha.jpg')
        ydm = YDMHttp()
        ydm.login()
        cid, result = ydm.decode('captcha.jpg', 5000, 20)
        driver.find_element_by_name('captcha').send_keys(result)
        driver.find_element_by_xpath('//div[@class="Login-content"]/form/button').click()
        # 倒立验证码
    else:
        captcha=WebDriverWait(driver,5).until(lambda driver:driver.find_element_by_class_name('Captcha-chineseImg'))
        captcha.screenshot(filename='captcha_a.jpg')
        ydm=YDMHttp()
        ydm.login()
        cid,result=ydm.decode('captcha_a.jpg',5000,20)
        driver.find_element_by_class_name('captcha').send_keys(result)
        driver.find_element_by_xpath('//div[@class="Login-content"]/form/button').click()




