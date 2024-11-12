# alert box - прикольно от этого какая польза интересно, вообще в дальнейшем буду ли я использовать
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://zimaev.github.io/dialog/")
    page.get_by_text("Диалог Alert").click()
    time.sleep(10)
    page.get_by_text("Диалог Confirmation").click()
    time.sleep(10)
    page.get_by_text("Диалог Prompt").click()
    time.sleep(10)
