from constants import BASE_URL


class TestGetBookings:
    def test_get_bookings(self, auth_session):

        get_booking = auth_session.get(f"{BASE_URL}/booking")
        assert get_booking.status_code == 200, "Ошибка при получении всех броней"
        assert len(get_booking.json()) > 1, "Количество броней меньше одной"

    def test_get_booking_by_wrong_firstname(self, auth_session):
        auth_session.params = {"firstname": "wrong_namehaha092$$"}

        get_booking = auth_session.get(f"{BASE_URL}/booking")
        assert get_booking.status_code == 200, "Ошибка при получении брони по имени"
        assert get_booking.json() == [], "Список с бронями является не пустым"

    def test_get_booking_by_wrong_lastname(self, auth_session):
        auth_session.params = {"lastname": "wrong_lastnamehaha092$$"}

        get_booking = auth_session.get(f"{BASE_URL}/booking")
        assert get_booking.status_code == 200, "Ошибка при получении брони по фамилии"
        assert get_booking.json() == [], "Список с бронями является не пустым"

    def test_get_booking_by_id(self, auth_session):
        get_booking = auth_session.get(f"{BASE_URL}/booking/989093922030346363636")
        assert get_booking.status_code == 404, "Получения брони"
        assert get_booking.text == "Not Found", "Текст ошибки некорретный"
