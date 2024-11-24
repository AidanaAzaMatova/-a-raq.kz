# чуть чуть вообще непонятно, терпим и учимся aiDoni
from playwright.sync_api import Page, expect


def test_network(page):
    page.route("**/register", lambda route: route.continue_(post_data='{"email": "user","password": "secret"}'))
    page.goto('https://reqres.in/')
    page.get_by_text(' Register - successful ').click()