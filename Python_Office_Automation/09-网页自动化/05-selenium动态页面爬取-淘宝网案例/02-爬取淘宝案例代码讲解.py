from selenium import webdriver
from selenium.webdriver.common.by import By #查询的方式
from selenium.webdriver.support.ui import WebDriverWait #智能等待
from selenium.webdriver.support import expected_conditions as EC #等待条件
from selenium.webdriver.common.action_chains import ActionChains #动作链
import time
import random
import re
browser = webdriver.Chrome()
browser.maximize_window()
# 等待变量
wait = WebDriverWait(browser, 60)
try:
    browser.get('https://www.taobao.com/')
    #id是q的输入框加载成功，停止等待
    tb_input = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
    )
    #搜索按钮加载成功，停止等待
    search_btn = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.search-button > button'))
    )
    tb_input.send_keys('手机')
    search_btn.click()

    wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist'))

    )
    total = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.total'))
    )
    total = total.text.strip()
    pat = re.compile(r'(\d+)')
    match_obj = pat.search(total)
    if match_obj != None:
        total = match_obj.group(1)
    print('total:', total)
    while True:
        ls = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="item J_MouserOnverReq  "]'))
        )
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(random.random()*2)
        print('len:', len(ls))
        for item in ls:
            title = item.find_element_by_xpath('.//div[@class="row row-2 title"]/a')
            detail_url = title.get_attribute('href')
            title = title.text.strip()
            print('title:', title)
            print('detail_url:', detail_url)
            price = item.find_elements_by_xpath('.//div[@class="price g_price g_price-highlight"]/strong')[0]
            price = price.text.strip()
            print('price:', price)
            shopname = item.find_elements_by_xpath('.//a[@class="shopname J_MouseEneterLeave J_ShopInfo"]/span[2]')[0]
            shopname = shopname.text.strip()
            print("shopname:", shopname)
            print('='*200)
            with open('../source_material/05/taobao.txt', mode="a", encoding='utf-8') as fp:
                fp.write('商品名：%s,价格：%s,店铺名：%s' % (title, price, shopname))
except Exception as e:
    print("错误")

browser.close()

