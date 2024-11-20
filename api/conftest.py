import pytest
import requests
from faker import Faker

from constants import HEADERS, BASE_URL

faker = Faker()


@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    session.headers.update(HEADERS)

    response = requests.post(f"{BASE_URL}/auth", headers=HEADERS, json={"username": "admin", "password": "password123"})
    assert response.status_code == 200, "Ошибка авторизации"
    token = response.json().get("token")
    assert token is not None, "В ответе не оказалось токена"

    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture()
def booking_data():
    return {
            "firstname": faker.first_name(),
            "lastname": faker.last_name(),
            "totalprice": faker.random_int(min=100, max=100000),
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-10-01",
                "checkout": "2024-12-01"
            },
            "additionalneeds": "Breakfast"
        }


@pytest.fixture()
def booking_id_for_test(auth_session, booking_data):
    create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
    assert create_booking.status_code == 200, "Ошибка при создании брони"
    booking_id = create_booking.json().get("bookingid")
    assert booking_id is not None, "Идентификатор брони не найден в ответе"
    return booking_id