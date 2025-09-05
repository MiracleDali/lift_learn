from playwright.sync_api import sync_playwright


# 启动playwright driver进程
p = sync_playwright().start()

# 启动浏览器 返回 Browser 类型对象
browser = p.chromium.launch(
    headless=False,   # 默认为True，无头模式
    executable_path=r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe"    # 使用本地浏览器打开
)

# 创建新的页面对象，返回 page 类型对象
page = browser.new_page()
page.goto("https://www.byhy.net/cdn2/files/selenium/stock1.html")
print(page.title())  # 打印页面标题

# 查询
page.locator('#kw').fill('通讯')
page.locator('#go').click()

# 以为playwright是异步的，所以不能使用time.sleep()
# 会导致一些奇怪的异常
page.wait_for_timeout(2000)

# 打印搜索内容
lcs = page.locator(".result-item").all()
for lc in lcs:
    print(lc.text_content())



# 关闭浏览器
browser.close()
# 关闭进程
p.stop()

 