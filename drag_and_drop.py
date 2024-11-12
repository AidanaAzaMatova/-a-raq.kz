# уже который код на playwright, но зачем непонятно
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://zimaev.github.io/draganddrop/')
    page.drag_and_drop("#drag", "#drop")
    time.sleep(10)
