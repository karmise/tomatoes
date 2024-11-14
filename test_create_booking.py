from constants import HEADERS, BASE_URL


class TestBookings:
    def test_create_booking(self, auth_session, booking_data):

        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "Идентификатор брони не найден в ответе"

        assert create_booking.json()["booking"]["firstname"] == booking_data["firstname"]
        assert create_booking.json()["booking"]["totalprice"] == booking_data["totalprice"]

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        assert get_booking. json()["lastname"] == booking_data["lastname"], "Заданная фамилия не совпадает"

        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, "Бронь не найдена"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 404, "Бронь не удалилась"
