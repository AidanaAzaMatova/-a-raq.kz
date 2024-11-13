# скачывает файл из сайта прикольно
import time, os
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com/upload-download")
    with page.expect_download() as download_info:
        page.locator("a:has-text(\"Download\")").click()

    download = download_info.value
    file_name = download.suggested_filename
    destination_folder_path = "./"
    download.save_as(os.path.join(destination_folder_path, file_name))
    time.sleep(10)

