# как на примере не работает и не показывает ошибок что я делаю не так думай aiDoni думай
from playwright.sync_api import expect
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")