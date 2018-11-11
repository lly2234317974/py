from selenium import webdriver
browser=webdriver.Chrome()
browser.get('http://www.huangye88.com/search.html?kw=%E5%A4%A7%E5%AE%97&type=company&')
browser.find_element_by_xpath('//*[@id="hs_3"]').click()#公司
browser.find_element_by_xpath('//*[@id="search_btn"]/input').click()#第一页
import time
time.sleep(3)
from selenium.webdriver.support.ui import WebDriverWait
# g=browser.find_element_by_xpath(".//*[@id='pagenum']")
# g.send_keys(16)
# # browser.find_element_by_xpath("")

page = browser.find_element_by_partial_link_text(u'下一页')
browser.execute_script("arguments[0].scrollIntoView(false);", page)
browser.find_element_by_xpath('//div[@class="pages"]/a').click()
# browser.find_element_by_xpath('//*[contains(text(),"确定")]').click()
#
# # WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, u'下一页'))).click()