from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(snapshots=True, sources=True, screenshots=True)
    page = context.new_page()
    page.goto("https://www.byhy.net/cdn2/files/selenium/sample1a.html")

    # 组选择 用逗号分隔不同选择器
    element = page.locator('#t1 > span , #t1 > p')
    print(element.all_inner_texts())

    # 父元素的第N个子节点 --> 正数
    element = page.locator('span:nth-child(2)')
    print(element.all_inner_texts())

    # 父元素的第N个子节点 --> 到数
    element = page.locator('span:nth-last-child(2)')
    print(element.all_inner_texts())
  
    # 父元素的第几个某类型的子节点 --> 正数
    element = page.locator('span:nth-of-type(2)')
    print(element.all_inner_texts())

    # 父元素的第几个某类型的子节点 --> 到数
    element = page.locator('span:nth-last-of-type(2)')
    print(element.all_inner_texts())

    # 兄弟元素定位
    element = page.locator('#t1 h3 ~ span')
    print(element.all_inner_texts())
    element = page.locator('#t1 h3 + span')
    print(element.all_inner_texts())

    context.tracing.stop(path="trace.zip")  