# CLI and pytest-playwright
import pytest
from playwright.sync_api import sync_playwright

# Пропустить тест браузером - вроде пропускает
@pytest.mark.skip_browser("firefox")
def test_visit_example(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")

# Запуск в определенном браузере - хер работает - вообще не работает, блин
@pytest.mark.only_browser("chromium")
def test_visit_example(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "storage_state": {
            "cookies": [
                {
                    "name": "stepik",
                    "value": "sd4fFfv!x_cfcstepik",
                    "url": "https://demo.playwright.dev/todomvc/#/"  # Замените на нужный URL
                },
            ]
        },
    }


def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")