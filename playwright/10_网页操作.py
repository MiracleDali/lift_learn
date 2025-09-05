from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context.set_default_timeout(10000)
    context.tracing.start(snapshots=True, screenshots=True, sources=True)
    page = context.new_page()

    page.goto('file:///D:/2_python_file/playwright/01.html')
    # 设置页面大小
    page.set_viewport_size({'width':800, 'height':600})
    page.wait_for_timeout(1000)

    # 点击链接打开新页面
    page.locator('exercise > a[name=link2byhy]').click()
    page.wait_for_timeout(1000)

    # 后退到前一个页面
    page.go_back()
    page.wait_for_timeout(1000)

    # 前进到下一个页面
    page.go_forward()
    page.wait_for_timeout(1000)

    # 刷新页面
    page.reload()
    page.wait_for_timeout(1000)

    # 获取当前页面的URL
    print(page.url)

    # 获取当前页面的html
    print(page.content())

    # 获取当前页面的标题
    print(page.title())


