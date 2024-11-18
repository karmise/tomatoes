from constants import BASE_URL


class TestCreateBookings:
    def test_create_booking(self, auth_session, booking_data):

        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "Идентификатор брони не найден в ответе"

        assert create_booking.json()["booking"]["firstname"] == booking_data["firstname"]
        assert create_booking.json()["booking"]["totalprice"] == booking_data["totalprice"]

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        booking_data_response = get_booking.json()
        assert booking_data_response["firstname"] == booking_data["firstname"], "Имя не совпадает с заданным"
        assert booking_data_response["lastname"] == booking_data["lastname"], "Фамилия не совпадает с заданной"
        assert booking_data_response["totalprice"] == booking_data["totalprice"], "Цена не совпадает с заданной"
        assert booking_data_response["depositpaid"] == booking_data["depositpaid"], "Статус депозита не совпадает"
        assert booking_data_response["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"], "Дата заезда не совпадает"
        assert booking_data_response["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"], "Дата выезда не совпадает"

        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, "Бронь не найдена"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 404, "Бронь не удалилась"
