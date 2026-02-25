from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(ApiClient):
    def client_user_api(self, request: CreateUserRequestDict) -> Response:
        return self.post("/api/v1/users", json=request)