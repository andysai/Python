#这个模块可以动态等待我们需要的元素出现，再实现find获取。
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#因为单纯用time的话，元素提前出现你就得多等时间，要是网速慢而没找到，就会报错。
from selenium.webdriver.common.by import By
#动态监测元素是否满足条件所需导入的模块
from selenium.webdriver.support import expected_conditions as EC

#虽然已经不显示界面了，但是浏览器还是会加载所有的信息，这样就会消耗不必要的资源，那么我们就可以禁止
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')

#虽然已经不显示界面了，但是浏览器还是会加载所有的信息，这样就会消耗不必要的资源，那么我们就可以禁止
chrome_options.add_argument('--disable-gpu')

#开始模拟打开网站
driver = webdriver.Chrome()
driver.get('https://www.kuaidi100.com/')

#打开后就等快递的输入框出现，出现了，我们才罢休
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'postid')))

#等到了，就输入单号
driver.find_element_by_id('postid').send_keys(input('请输入快递单号'))

#输入单号回车，就点击查询按钮
driver.find_element_by_id('query').click()

#显式等待完整的写法应该是这样的，等搜索结果出现
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_all_elements_located( (By.CLASS_NAME,'context' ) ) )

#打印物流当前状态
nowdata = driver.find_element_by_class_name('contex')
print(nowdata.text)

#打印历史进程
details = driver.find_elements_by_class_name('context')
for detail in details:
    print(detail.text)
