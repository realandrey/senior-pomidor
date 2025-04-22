import pytest
import requests

from faker import Faker

from constant import HEADERS, BASE_URL

faker = Faker()

@pytest.fixture(scope="session")
def auth_session():
    """Создаёт сессию с авторизацией и возвращает объект сессии."""
    session = requests.session()
    session.headers.update(HEADERS)

    auth_response = session.post(
        f"{BASE_URL}/api/v1/login/access-token",
        data = {"username" : "real_andreyka@mail.ru", "password" : "Test@123"}
    )
    assert auth_response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = auth_response.json().get('token')
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({'Cookie':f"token={token}"})
    return session

@pytest.fixture()
def item_data():
    """Генерирует данные для создания нового элемента."""
    return {
        "title": faker.title(),
        "description": faker.description()
    }