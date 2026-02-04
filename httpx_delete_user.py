import httpx
import time
from tools.fakers import get_random_email


print('Create new user...')
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "Ivanov",
    "firstName": "Dimqa",
    "middleName": "Petrovich"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print(create_user_response.status_code)
print('User created: ', create_user_response_data)


#Авторизуемся
print('Login in system...')
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(login_response.status_code)
print('Login successfull ',login_response_data)


#Получаем токен
print('get auth token...')
headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
print('Done. Token: ', login_response_data['token']['accessToken'])


#Удаляем
print('Delete user...')
delete_user = httpx.delete(
f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=headers
)
print('User deleled: ', delete_user.status_code)