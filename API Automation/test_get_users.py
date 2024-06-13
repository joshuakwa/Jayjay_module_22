import requests
from assertpy import assert_that


def test_get_list_users():
    req = requests.get("https://reqres.in/api/users")
    response = req.json()
    data = response.get('data')

    assert_that(req.status_code).is_equal_to(200)
    assert_that(req.elapsed.total_seconds()).is_less_than_or_equal_to(2)

    for x in data:
        assert_that(x.get('email')).is_not_none()
        assert_that(x.get('id')).is_not_none()
        assert_that(x.get('avatar')).is_not_none()
        assert_that(x.get('first_name')).is_not_none()