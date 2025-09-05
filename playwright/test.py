import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.baidu.com/")
    page.get_by_role("button", name="百度一下").click()
    expect(page).to_have_title(re.compile("百度一下"))
  
    assert "baidu" in page.url