import requests
from assertpy import assert_that


def test_create_user():
    payload = {
        "name": "joshua",
        "job": "QA"
    }

    req = requests.post("https://reqres.in/api/users", json=payload)
    response = req.json()

    assert_that(req.status_code).is_equal_to(201)
    assert_that(req.elapsed.total_seconds()).is_less_than_or_equal_to(2)
    assert_that(response.get('name')).is_equal_to("joshua")
    assert_that(response.get("job")).is_equal_to("QA")


