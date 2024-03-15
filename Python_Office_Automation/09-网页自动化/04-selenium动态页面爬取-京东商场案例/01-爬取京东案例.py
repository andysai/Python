from selenium import webdriver
import time
import random

driver = webdriver.Chrome()
url = 'https://www.jd.com/'
driver.get(url)

tb_input = driver.find_element_by_css_selector('#key')  # 搜索输入框
search_btn = driver.find_element_by_css_selector('.button')  # 搜索按钮

tb_input.send_keys('手机')
time.sleep(2)
search_btn.click()
time.sleep(2)
for page in range(5):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(random.random() + 1)
    # 商品信息的提取
ls = driver.find_elements_by_css_selector('.gl-item')
for info in ls:
    title = info.find_element_by_css_selector('.p-name.p-name-type-2 a').text.strip()
    print('title:', title)
    price = info.find_element_by_css_selector('div.p-price > strong > i').text.strip()
    print('price:', price)
    shop = info.find_element_by_css_selector('span.J_im_icon > a').text.strip()
    print('shop:', shop)
    comments = info.find_element_by_css_selector('div.p-commit > strong > a').text.strip()
    print('comments:', comments)
    print("=" * 200)
    with open('../source_material/04/jd.txt', mode="a", encoding='utf-8') as fp:
        fp.write('商品名：%s,价格：%s,店铺名：%s,销量：%s\n' % (title, price, shop, comments))
# 翻页
time.sleep(random.random() * 2)
btn_next = driver.find_element_by_css_selector('a.pn-next')
btn_next.click()

driver.close()
