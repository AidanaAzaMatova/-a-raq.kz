# Работа с несколькими вкладками(Tabs)
import time, os
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://zimaev.github.io/tabs/")
    with page.context.expect_page() as tab:
        page.get_by_text("Переход к Dashboard").click()

    new_tab = tab.value
    assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"
    sign_out = new_tab.locator('.nav-link', has_text='Sign out')
    assert sign_out.is_visible()
    time.sleep(10)

