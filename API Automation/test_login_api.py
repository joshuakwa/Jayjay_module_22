import requests
from assertpy import assert_that


def test_login():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    req = requests.post("https://reqres.in/api/login", json=payload)
    response = req.json()

    assert_that(req.status_code).is_equal_to(200)
    assert_that(req.elapsed.total_seconds()).is_less_than_or_equal_to(2)
    assert_that(response).is_not_empty()
    assert_that(response.get('token')).is_not_none()

