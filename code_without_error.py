from playwright.sync_api import Playwright, sync_playwright, expect

# рабочий код, хех, благодаря коментариям. хорошо что есть люди более умные. надо учиться
def test_auth() -> None:
    playwright: Playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    context.close()
    browser.close()