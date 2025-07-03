from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器对象
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)

driver.get('https://www.baidu.com')

# xpath结合基本属性定位  可以使用 and 来添加多个条件
el1 = driver.find_element(By.XPATH, ".//input[@id='kw' and @class='s_ipt' and @name='wd']")
print(el1)

# xpath的文本定位
el2 = driver.find_element(By.XPATH, ".//span[text()='换一换']")
print(el2.text)

# xpath的层级定位
el3 = driver.find_element(By.XPATH, ".//form[@id='form']/span/input")
print(el3)
# xpath的层级定位 -- 父级定位
el4 = driver.find_element(By.XPATH, ".//input[@class='s_ipt']/parent::span")
print(el4)
# xpath的层级定位 -- 哥哥元素定位
el5 = driver.find_element(By.XPATH, ".//input[@class='s_ipt']/preceding-sibling::span")
print(el5)
# xpath的层级定位 -- 弟弟元素定位
el6 = driver.find_element(By.XPATH, ".//input[@class='s_ipt']/following-sibling::span")
print(el6)