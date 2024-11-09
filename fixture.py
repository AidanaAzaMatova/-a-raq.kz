# Люблю когда все работает. Люблю коды без ошибок.
# Вот бы в жизне так. Обидно.
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.fixture
def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()

def test_add_todo(browser_fixture):
    pass