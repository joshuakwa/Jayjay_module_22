import requests
from assertpy import assert_that


def test_negative_login():
    payload = {
        "email": "negative_login@reqres.in",
        "password": "negative"
    }

    req = requests.post("https://reqres.in/api/login", json=payload)
    response = req.json()

    assert_that(req.status_code).is_equal_to(400)
    assert_that(req.elapsed.total_seconds()).is_less_than_or_equal_to(2)
    assert_that(response).is_not_empty()
    assert_that(response.get('error')).is_equal_to("user not found")

