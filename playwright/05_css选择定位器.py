
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(snapshots=True, sources=True, screenshots=True)
    page = context.new_page()
    page.goto('https://www.byhy.net/cdn2/files/selenium/sample1.html')


    # 根据属性选择元素
    element = page.locator('[href="http://www.miitbeian.gov.cn"]')
    print(element.inner_text())

    # 选择属性值包含某个字符串的元素
    element = page.locator('[href*="miitbeian"]')
    print(element.inner_text())

    # 选择属性值以某个字符串开头的元素
    element = page.locator('[href^="http://"]')
    print(element.inner_text())

    # 选择属性值以某个字符串结尾的元素
    element = page.locator('[href$=".cn"]')
    print(element.inner_text())

    # 使用一个元素的多个属性进行定位,并输入文字
    element = page.locator('[type="text"][id="searchtext"]').fill('hello')
    page.wait_for_timeout(2000)



    

    context.tracing.stop(path="trace.zip")
 