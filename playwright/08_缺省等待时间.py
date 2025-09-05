from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context = browser.new_context()
    # 修改缺省等待时间
    context.set_default_timeout(10000)

    page = context.new_page()
    page.goto('https://www.byhy.net/cdn2/files/selenium/stock1.html')

    page.locator('[id="kw"]').fill('通讯')
    page.locator('[id="go"]').click(timeout=5000)

    element = page.locator('div[id="1"] > .name')
    # 单个步骤创建超时时间
    print(element.inner_text(timeout=5000))

    page.wait_for_timeout(2000)

    