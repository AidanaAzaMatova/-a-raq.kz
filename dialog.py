# dialog - хер надо, вообще в дальнейшем буду ли я использовать, вообще прикольно зачем делаешь весь этот путь если на практике не увидела
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_text("Диалог Confirmation").click()
    time.sleep(10)
