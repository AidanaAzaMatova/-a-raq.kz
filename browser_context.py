# код работает, но как он работает зачем этот pytest
# сложно когда учишься одна вот бы добродушного человека который будет обяснять принцип работы
# больно, печально, больно (как высказал свое мнение один из моих учителей)
import pytest
from playwright.sync_api import sync_playwright


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