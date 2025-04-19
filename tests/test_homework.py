from constant import BASE_URL

class TestBookings:

    def test_create_booking(self, booking_data, auth_session):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        booking_data_response = get_booking.json()
        assert booking_data_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert booking_data_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert booking_data_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
        assert booking_data_response['bookingdates']['checkin'] == booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert booking_data_response['bookingdates']['checkout'] == booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"

    def test_update_booking(self, booking_data, auth_session, created_booking):
        response = auth_session.put(f"{BASE_URL}/booking/{created_booking}", json=booking_data)
        assert response.status_code == 200, "Ошибка при обновлении данных"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{created_booking}")
        assert get_booking.status_code == 200, "Не удалось получить обновлённое бронирование"

        booking_data_response = get_booking.json()
        assert booking_data_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert booking_data_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert booking_data_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
        assert booking_data_response['bookingdates']['checkin'] == booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert booking_data_response['bookingdates']['checkout'] == booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"

    def test_partial_update_booking(self, auth_session, created_booking, booking_data):
        partial_update_data = {"totalprice": 5000}  # Обновляем только цену

        response = auth_session.patch(f"{BASE_URL}/booking/{created_booking}", json=partial_update_data)
        assert response.status_code == 200, "Ошибка при обновлении данных"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{created_booking}")
        assert get_booking.status_code == 200, "Не удалось получить обновлённое бронирование"

        booking_data_response = get_booking.json() # Проверяем, что только обновлённые данные изменены
        assert booking_data_response["totalprice"] == partial_update_data["totalprice"],  "Цена не обновилась"

        assert booking_data_response['firstname'] == booking_data['firstname'], "Имя не должно было измениться"
        assert booking_data_response['lastname'] == booking_data['lastname'], "Фамилия не должна была измениться"
        assert booking_data_response['depositpaid'] == booking_data[
            'depositpaid'], "Статус депозита не должен был измениться"
        assert booking_data_response['bookingdates']['checkin'] == booking_data['bookingdates'][
            'checkin'], "Дата заезда не должна была измениться"
        assert booking_data_response['bookingdates']['checkout'] == booking_data['bookingdates'][
            'checkout'], "Дата выезда не должна была измениться"

    def test_get_all_bookings(self, auth_session, created_booking):
        response = auth_session.get(f"{BASE_URL}/booking")
        assert response.status_code == 200, "Не удалось получить id бронирований"

    def test_delete_booking(self, auth_session, created_booking):
        response = auth_session.delete(f"{BASE_URL}/booking/{created_booking}")
        assert response.status_code == 201, f"Ошибка при удалении букинга с ID {created_booking}"

        response = auth_session.get(f"{BASE_URL}/booking/{created_booking}")
        assert response.status_code == 404, "Букинг не был удален"
