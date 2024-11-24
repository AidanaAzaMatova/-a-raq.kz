
# он работает, но как iDONi вообще не понимает, хех
def test_inventory(page):
    response = page.request.get('https://petstore.swagger.io/v2/store/inventory')
    print(response.status)
    print(response.json())