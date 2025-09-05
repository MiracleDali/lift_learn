from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(snapshots=True, sources=True, screenshots=True)
    page = context.new_page()
    page.goto('https://www.byhy.net/cdn2/files/selenium/test4.html')


    # 处理 allert 弹出对话框 的 回调函数
    # 在没有定义回调函数时，默认点击取消
    def handleDlg(dialog):
        # 等待一秒
        page.wait_for_timeout(1000)
        # 点击确定
        if dialog.type == 'alert':
            dialog.accept()
        # 点击取消
        if dialog.type == 'confirm':
            dialog.dismiss()
        # 输入内容
        if dialog.type == 'prompt':
            dialog.accept('hello')
        # 打印弹出框信息
        print(dialog.message)

    page.on('dialog', handleDlg)

    # 触发 alert 弹出对话框
    page.wait_for_timeout(1000)
    page.locator('button[id="b1"]').click()
    page.wait_for_timeout(1000)


    # confirm 确认弹窗
    page.wait_for_timeout(1000)
    page.locator('button[id="b2"]').click()
    page.wait_for_timeout(1000)


    # prompt 提示输入弹窗
    page.wait_for_timeout(1000)
    page.locator('button[id="b3"]').click()
    page.wait_for_timeout(1000)