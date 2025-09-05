from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("file:///D:/2_python_file/playwright/01.html")

    # 根据 role 定位
    element = page.get_by_role('alert')
    print(element.inner_text())

    # 根据 role 定位
    # progress 默认带有 role属性
    element = page.get_by_role('progressbar')
    print(element.get_attribute('value'))
    print(element.get_attribute('max'))

    # 根据 css 选择器定位
    element = page.locator('[type="search"]')
    element.fill('hello')

    # page.wait_for_timeout(3000)
    # # 调转页面
    # element = page.get_by_role('link', name='白月黑羽教程').click()
    # page.wait_for_timeout(3000)

    # 根据 label 定位
    element = page.get_by_label('Username').fill('hellott')
    element = page.get_by_label('Password').fill('hellooo')
    page.wait_for_timeout(3000)

