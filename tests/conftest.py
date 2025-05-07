import pytest
import requests
from faker import Faker
from playwright.sync_api import sync_playwright

from constant import HEADERS, BASE_URL

faker = Faker()

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start() # Далее, используя объект playwright, можно запускать браузер и работать с ним
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture(scope="session")
def auth_session():
    """Создаёт сессию с авторизацией и возвращает объект сессии."""
    session = requests.Session()
    session.headers.update(HEADERS)

    auth_response = session.post(f"{BASE_URL}/auth", json={"username": "admin", "password": "password123"})
    assert auth_response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = auth_response.json().get("token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session

@pytest.fixture()
def booking_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": "Breakfast"
    }

@pytest.fixture()
def created_booking(auth_session, booking_data):
    response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
    assert response.status_code == 200, "Ошибка создания бронирования"
    booking_id = response.json().get("bookingid")
    assert booking_id is not None, "Не получили bookingid"
    return booking_id