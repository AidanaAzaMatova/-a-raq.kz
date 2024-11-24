# это тоже заработал, интересно, копируешь вставляешь заупскаешь
# у тебя все работает, при этом не понимает человек который выполняет эти действия
# это нормальное явленение когда человек не понимает
def test_add_user(page):
    data = [
              {
                "id": 9743,
                "username": "fsd",
                "firstName": "fff",
                "lastName": "ggg",
                "email": "bbb",
                "password": "tt",
                "phone": "333",
                "userStatus": 0
              }
            ]
    header = {
        'accept': 'application/json',
        'content-Type': 'application/json'
    }
    response = page.request.post('https://petstore.swagger.io/v2/user/createWithArray',data=data, headers=header)
    print(response.status)
    print(response.json())