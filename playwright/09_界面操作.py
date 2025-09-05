from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context.set_default_timeout(30000)
    context.tracing.start(snapshots=True, sources=True, screenshots=True)

    page = context.new_page()
    page.goto('file:///D:/2_python_file/playwright/01.html')
    page.wait_for_timeout(1000)

    element = page.locator('#source')
    # inner_text() 只能获取页面上的文本
    # text_content() 可以获取页面源码（html）里面的文本
    print(element.text_content())

    # 使用 get_attribute() 获取属性值
    element_attribute = page.locator('a[name^="link"]')
    print(element_attribute.get_attribute('href'))

    # click() 单击方法
    page.locator('input[id=password-input]').click()
    page.wait_for_timeout(1000)

    # dblclick() 双击方法
    page.locator('p#source > span[id="text"]').get_by_text('看一下').dblclick()
    page.get_by_text('看一下').dblclick()
    page.wait_for_timeout(1000)

    # hover() 鼠标悬停方法
    page.locator('body > exercise > a[name=link2byhy]').hover()
    page.wait_for_timeout(1000)

    # wait_for() 等待方法 元素会出现但是不知道什么时候出现
    wait_for = page.locator('div.dynamic-content > p')
    wait_for.wait_for()
    print(wait_for.text_content())

    # 判断元素是否可见
    is_visible = page.locator('div.dynamic-content > p').is_visible()
    print(is_visible)

    # 单行文本输入框和多行文本输入框
    page.locator('input[aria-label="Username"]').fill('hello')
    page.wait_for_timeout(1000)

    # 获取输入框内容
    input_value = page.locator('input[aria-label="Username"]').input_value()
    print(input_value)

    # 清空输入框
    page.locator('input[aria-label="Username"]').clear()
    page.wait_for_timeout(1000)

    # 文件输入框
    lc = page.locator('input#fileInput')
    lc.set_input_files(r"C:\Users\Administrator\Desktop\新建文本文档.txt")
    # 多选需要用列表括住
    # lc.set_input_files([r"\1.txt", r"\2.txt"])
    page.wait_for_timeout(1000)

    # radio 单选框
    page.locator('input[type=radio][name=gender]#zandouji').check()
    page.wait_for_timeout(1000)
    # 获取当前已经选择的选框
    lcs = page.locator('input[type=radio][name=gender]:checked').all()
    print('当前选择的单选框是：', [lc.get_attribute('id') for lc in lcs])
    page.wait_for_timeout(1000)

    # Checkbox 多选框
    page.locator('input[type=checkbox][id=music]').check()
    page.wait_for_timeout(1000)
    page.locator('input[type=checkbox][id=sports]').check()
    page.locator('input[type=checkbox][id=read]').check()
    # 取消选择
    page.locator('input[type=checkbox][id=music]').uncheck()
    page.wait_for_timeout(1000)
    # 获取当前已经选择的多选框
    lcs = page.locator('input[type=checkbox]:checked').all()
    print('当前选择的多选框是：', [lc.get_attribute('id') for lc in lcs])

    # 单选下拉菜单 
    page.locator('select#select').select_option(value='option2')  # 根据value属性值选择
    page.wait_for_timeout(500)
    page.locator('select#select').select_option(label='选项3')    # 根据label文本属性值选择
    page.wait_for_timeout(500)
    # 获取当前已经选择单选下拉菜单
    lcs = page.locator('select#select option:checked').all_inner_texts()
    print('当前选择单选下拉菜单是：', lcs)
    # 清空全部选择
    page.locator('select#select').select_option([])
    page.wait_for_timeout(500)

    # 根据value属性值选择多选下拉菜单
    page.locator('select[id=hobbies]').select_option(value=['music', 'sports'])
    page.wait_for_timeout(1000)
    # 根据label文本属性值选择多选下拉菜单
    page.locator('select[id=hobbies]').select_option(label=['阅读', '运动'])
    page.wait_for_timeout(1000)
    # 获取当前已经选择的多选下拉菜单
    lcs = page.locator('select[id=hobbies] option:checked').all_inner_texts()
    print('当前选择多选下拉菜单是：', lcs)
    # 清空全部选择
    page.locator('select[id=hobbies]').select_option([])
    page.wait_for_timeout(1000)