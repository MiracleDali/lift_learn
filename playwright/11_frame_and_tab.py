from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(snapshots=True, sources=True, screenshots=True)
    page = context.new_page()
    page.goto("https://www.byhy.net/cdn2/files/selenium/sample2.html")
    page.wait_for_timeout(1000)

    # 获取所有frame
    frames = page.frames
    print(frames)

    # 进入某个frame
    frame = page.frame_locator('iframe[src="sample1.html"][id=frame1]')
    # 获取frame中的元素
    animal = frame.locator('div.animal').all_inner_texts()
    print(animal)
    # 在iframe内输入
    frame.locator('input[type="text"][id="searchtext"]').fill("hello")
    page.wait_for_timeout(1000)

    # 点击外部按钮
    page.click('div > button#outerbutton')
    page.wait_for_timeout(1000)