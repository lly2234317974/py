from selenium import webdriver
import random
chromeOptions=webdriver.ChromeOptions()
proxy=['http://49.67.66.187:36410']
proxy_a=random.choice(proxy)
chromeOptions.add_argument('--proxy-server=http://49.67.66.187:36410')
bromer=webdriver.Chrome(chrome_options=chromeOptions)
bromer.get('http://httpbin.org/ip')
print(bromer.page_source)
bromer.quit()