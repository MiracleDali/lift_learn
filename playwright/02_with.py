import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.baidu.com/")
    page.get_by_role("button", name="百度一下").click()