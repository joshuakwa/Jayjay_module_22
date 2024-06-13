import requests
from assertpy import assert_that


def test_get_single_user():
    req = requests.get("https://reqres.in/api/users/2")
    response = req.json()
    data = response.get('data')

    assert_that(req.status_code).is_equal_to(200)
    assert_that(req.elapsed.total_seconds()).is_less_than_or_equal_to(2)
    assert_that(data.get('email')).is_not_none()
    assert_that(data.get('id')).is_not_none()
    assert_that(data.get('avatar')).is_not_none()
    assert_that(data.get('first_name')).is_not_none()

