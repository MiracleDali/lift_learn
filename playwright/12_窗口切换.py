from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(snapshots=True, sources=True, screenshots=True)
    page = context.new_page()
    page.goto("https://www.byhy.net/cdn2/files/selenium/sample3.html")
    page.wait_for_timeout(1000)

    # 打开新窗口
    page.locator('a[href="http://www.bing.com"]').click()
    page.wait_for_timeout(1000)

    # 获取所有窗口
    handles = page.context.pages
    print(handles)

    # 切换窗口
    new_page = page.context.pages[1]
    # 在切换到的窗口中执行操作
    new_page.locator('div[id=sb_form_c] > input[id=sb_form_q][name="q"]').fill('playwright')
    new_page.wait_for_timeout(1000)

    # 显示指定的页面
    page.bring_to_front()
    page.locator('button[id=outerbutton]').click()
    page.wait_for_timeout(1000)

    # 关闭某个网页
    new_page.close()
    page.wait_for_timeout(1000)
