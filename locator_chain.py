import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://zimaev.github.io/navbar/')
    page.locator("#navbarNavDropdown >> li:has-text('Company')").click()
    time.sleep(10)