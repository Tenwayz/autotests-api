import httpx

login_payload = {
    "email": "Dimqa@example.com",
    "password": "password"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print('Статус код: ', login_response.status_code)
print('Полученые данные: ', login_response_data)

headers = {'Authorization': 'Bearer ' + login_response_data['token']['accessToken']}
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
response_data = response.json()

print('Статус код: ', response.status_code)
print('Полученые данные: ', response_data)