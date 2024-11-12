# чтобы заработать этот код надо создать файл с названием hello.txt, цель загрузить файл если не создадите код выдаст вам ошибку, хех
# мысли aiDoni, учи, учи и практикуйся
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://zimaev.github.io/upload/')
    with page.expect_file_chooser() as fc_info:
        page.locator("#formFile").click()
    file_chooser = fc_info.value
    file_chooser.set_files("hello.txt")
    time.sleep(10)

