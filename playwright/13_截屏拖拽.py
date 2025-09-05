from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(snapshots=True, sources=True, screenshots=True)
    page = context.new_page()
    page.goto("https://www.byhy.net/etc/playwright/05/#_3")
    page.wait_for_timeout(2000)

    # 截屏当前页面可见内容
    page.screenshot(path="te.png")
    # 截屏当前页面所有内容
    page.screenshot(path="te2.png", full_page=True)

    context.tracing.stop(path="trace.zip")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(snapshots=True, sources=True, screenshots=True)
    page = context.new_page()
    page.goto("file:///D:/2_python_file/playwright/01.html?")
    page.wait_for_timeout(1000)

    # 使用 drag_and_drop 拖拽
    page.locator('p > span[id="text"]').select_text()
    page.wait_for_timeout(500)
    page.drag_and_drop('p > span[id="text"]', 'form > input[type="text"]')
    page.wait_for_timeout(2000)

    # 使用 drag_to
    ele = page.locator('p > span[id="text"]').select_text()
    ele = page.locator('p > span[id="text"]')
    page.wait_for_timeout(1000)
    ele.drag_to(page.locator('form > input[type="text"]'))
    page.wait_for_timeout(2000)

    # 使用拖拽
    page.locator('p > span[id="text"]').drag_to(page.locator('form > input[type="text"]'))
    page.wait_for_timeout(2000)
