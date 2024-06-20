import requests
from assertpy import assert_that


def test_negative_update_user():
    payload = {
        "job": "QA Engineer"
    }

    req = requests.put("https://reqres.in/api/users/2", json=payload)
    response = req.json()

    assert_that(req.status_code).is_equal_to(200)
    assert_that(req.elapsed.total_seconds()).is_less_than_or_equal_to(2)
    assert_that(response.get('name')).is_none()
    assert_that(response.get("job")).is_equal_to("QA Engineer")


