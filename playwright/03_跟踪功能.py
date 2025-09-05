"""

"""
import pathlib
base_path = pathlib.Path(__file__).parent
print(base_path)

from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=True)

context = browser.new_context()
context.tracing.start(snapshots=True, sources=True, screenshots=True)

page = context.new_page()
page.goto("https://www.byhy.net/cdn2/files/selenium/sample1.html")
print(page.title())  


# # 使用 tag 标签 定位并获取内部文本
# # 当获取多个元素时，使用 all_inner_texts() 或者 all()
# locators = page.locator('div').all_inner_texts()
# for i in locators:
#     print(i) 

# # 使用 id 定位 并输入文字
# id_locators = page.locator('#searchtext').fill('测试')
# page.wait_for_timeout(2000)

# # 使用 class 定位
# # ('.chinese.student') 这是两个class属性
# class_locator = page.locator('.chinese.student')  
# print(class_locator.inner_text())


# # 获取多个标签元素-对象
# locators = page.locator('div').all()
# for i in locators:
#     print(i.inner_text())

# # 获取多个 id属性 元素-文本
# locator_list = page.locator('#bottom').all_inner_texts()
# print(locator_list)

# # 获得 class属性 元素数量
# locators_count = page.locator('.animal').count()
# print(locators_count)

# 获得 class属性 第一个或者最后一个元素
locator = page.locator('.animal')
first = locator.first.inner_text()
print(first)
last = locator.last.inner_text()
print(last)

# 获得 class属性 第n个元素
nth = locator.nth(1).inner_text()
print(nth)

# 获得id元素对象的内部标签元素对象
lct = page.locator('#bottom')
print(lct.locator('span').all_inner_texts())

# 选择非直接子元素
no_direct_element = page.locator('#bottom span')
print(no_direct_element.all_inner_texts())

# 选择直接子元素
direct_element = page.locator('#bottom > .footer1 > span')
print(direct_element.all_inner_texts())


# 根据属性选择


context.tracing.stop(path="trace.zip")
browser.close()
p.stop()


