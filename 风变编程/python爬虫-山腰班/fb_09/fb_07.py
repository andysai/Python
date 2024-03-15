import requests,time
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
res_html = driver.page_source
#print(res_html)
driver.close()
res = BeautifulSoup(res_html,'html.parser')
suops = res.find_all('label')
for suop in suops:
    print(suop.text)

