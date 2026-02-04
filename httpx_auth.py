import httpx

login_payload = {
    "email": "Dimqa@example.com",
    "password": "password"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print('Response_status: ', login_response.status_code)
print('Response: ', login_response_data)




refresh_payload = {
    "refreshToken": login_response_data['token']['refreshToken'],
}
refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

print('Response_status: ', refresh_response.status_code)
print('Response: ', refresh_response_data)
