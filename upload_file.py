from importlib.metadata import files

import httpx

from tools.fakers import get_random_email

new_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
new_user = httpx.post('http://localhost:8000/api/v1/users', json=new_user_payload)
new_user_response_data = new_user.json()
print(new_user_response_data)



login_user_payload = {
    "email": new_user_payload['email'],
    "password": new_user_payload['password']
}
login_user = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_user_payload)
login_user_response_data = login_user.json()
print("Login successfull")
print(login_user_response_data)


create_headers = {
    "Authorization": f"Bearer {login_user_response_data['token']['accessToken']}"
}

create_file_response = httpx.post(
    'http://localhost:8000/api/v1/files',
    data = {"filename": "my_file.png", "directory": "images"},
    files = {"upload_file": open('./testdata/files/my_file.png', 'rb')},
    headers = create_headers
)
create_file_response_data = create_file_response.json()
print(create_file_response_data)