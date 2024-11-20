from constants import BASE_URL
from faker import Faker

faker = Faker()

class TestUpdateBookings:

    def test_update_booking_with_the_same_data(self, auth_session, booking_id_for_test, booking_data):

        update_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id_for_test}", json=booking_data)
        assert update_booking.status_code == 200, "Ошибка при обновлении брони"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id_for_test}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        booking_data_response = get_booking.json()
        assert booking_data_response["firstname"] == booking_data["firstname"], "Имя не совпадает с заданным"
        assert booking_data_response["lastname"] == booking_data["lastname"], "Фамилия не совпадает с заданной"
        assert booking_data_response["totalprice"] == booking_data["totalprice"], "Цена не совпадает с заданной"
        assert booking_data_response["depositpaid"] == booking_data["depositpaid"], "Статус депозита не совпадает"
        assert booking_data_response["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"], "Дата заезда не совпадает"
        assert booking_data_response["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"], "Дата выезда не совпадает"

        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id_for_test}")
        assert deleted_booking.status_code == 201, "Бронь не найдена"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id_for_test}")
        assert get_booking.status_code == 404, "Бронь не удалилась"

    def test_update_booking_with_new_firstname(self, auth_session, booking_id_for_test, booking_data):
        booking_data["firstname"] = faker.first_name()

        update_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id_for_test}", json=booking_data)
        assert update_booking.status_code == 200, "Ошибка при обновлении брони"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id_for_test}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        booking_data_response = get_booking.json()
        assert booking_data_response["firstname"] == booking_data["firstname"], "Имя не совпадает с заданным"

        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id_for_test}")
        assert deleted_booking.status_code == 201, "Бронь не найдена"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id_for_test}")
        assert get_booking.status_code == 404, "Бронь не удалилась"

    def test_update_booking_with_invalid_firstname(self, auth_session, booking_id_for_test,  booking_data):
        booking_data["firstname"] = True

        update_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id_for_test}", json=booking_data)
        assert update_booking.status_code == 500, "Бронь обновлена с недопустимым именем!"

        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id_for_test}")
        assert deleted_booking.status_code == 201, "Бронь не найдена"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id_for_test}")
        assert get_booking.status_code == 404, "Бронь не удалилась"

    def test_update_booking_with_non_existent_key(self, auth_session, booking_id_for_test,  booking_data):
        booking_data["childrenscount"] = 3

        update_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id_for_test}", json=booking_data)
        assert update_booking.status_code == 400, "Бронь обновлена с несуществующим ключом!"

        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id_for_test}")
        assert deleted_booking.status_code == 201, "Бронь не найдена"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id_for_test}")
        assert get_booking.status_code == 404, "Бронь не удалилась"

    def test_update_booking_with_non_existent_id(self, auth_session,  booking_data):
        update_booking = auth_session.put(f"{BASE_URL}/booking/55555555555555555555555555555", json=booking_data)
        assert update_booking.status_code == 405, "Обновлена несуществующая бронь!"

