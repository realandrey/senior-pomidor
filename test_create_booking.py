import requests
import pytest

class TestBooking:
    BASE_URL = "https://restful-booker.herokuapp.com/"
    HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
    json = {"username" : "admin", "password" : "password123"}

    def get_token(self):
        response = requests.post(f"{self.BASE_URL}/auth", headers=self.HEADERS, json=self.json)
        assert response.status_code == 200, "Ошибка авторизации"
        token = response.json().get("token")
        assert token is not None, "В ответе не оказалось токена"
        return token

    def test_create_booking(self):
        session = requests.Session()
        session.headers.update(self.HEADERS)

        token = self.get_token()
        session.headers.update({"Cookie": f"token={token}"})

        booking_data = {
        "firstname": "Sally",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
        }

        create_booking = session.post(f"{self.BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "Идентификатор брони не найден в ответе"

        assert create_booking.json()["booking"]["firstname"] == "Sally", "Заданное имя не совпадает"
        assert create_booking.json()["booking"]["totalprice"] == 111, "Заданное стоимость не совпадает"