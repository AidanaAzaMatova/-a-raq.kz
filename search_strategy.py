# стратегия есть и стратегия, хер поймешь зачем использовать
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#skills', value=["playwright", "python"])
    time.sleep(10)

