# зачем записать в курс не рабочий код не пойму
# или я не понимаю, терпи и учи даже chatpgpt не дает ответ или ты не умеешь
# получать ответ, бесишь, iDoNi
from playwright.sync_api import Page, Route, expect


def test_intercepted(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        json = response.json()
        json["tags"] = ["open", "solutions"]
        route.fulfill(json=json)

    page.route("**/api/tags", handle_route)

    page.goto("https://demo.realworld.io/")
    sidebar = page.locator('css=div.sidebar')
    expect(sidebar.get_by_role('link')).to_contain_text(["open", "solutions"])