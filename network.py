# чуть чуть вообще непонятно, терпим и учимся aiDoni
from playwright.sync_api import Page, expect


def test_listen_network(page: Page):
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto('https://osinit.ru/')