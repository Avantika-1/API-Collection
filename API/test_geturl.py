import allure
import pytest
import requests


@allure.title("get request - landing screen")
@allure.tag("sanity")
@pytest.mark.sanity
def test_get_landing_screen():
    url = "https://api.testaonline.com"
    response_data = requests.get(url)
    print("Response Text:", response_data)
    assert response_data.status_code == 200


@pytest.mark.regression
def test_get_landing_screen_invalid():
    url = "https://api.testaonline.com/invalid"
    response_data = requests.get(url)
    print("Response Text:", response_data)
    assert response_data.status_code == 404


@pytest.mark.sanity
@allure.description("Login with positive scenario")
def test_signin():
    base_url = "https://api.testaonline.com"
    base_path = "/api/login-user"
    url1 = base_url + base_path
    headers = {
        "content-type": "application/json",
        }
    payload = {
        "device": "desktop",
        "browser": "Chrome",
        "addreiss": "110.235.232.200",
        "latitude": 28.5147136,
        "longitude": 77.2112384,
        "email": "avantika@radiantinfonet.com",
        "password": "Test@1234"
    }
    response_data = requests.post(url=url1, headers=headers, json=payload)

    print("Response Text:", response_data)
    assert response_data.status_code == 200

@pytest.mark.regression
@allure.description("negative scenario login")
def test_signin():
    base_url = "https://api.testaonline.com"
    base_path = "/api/login-user"
    url1 = base_url + base_path
    headers = {
        "content-type": "application/json",
        }
    payload = {
        "device": "desktop",
        "browser": "Chrome",
        "addreiss": "110.235.232.200",
        "latitude": 28.5147136,
        "longitude": 77.2112384,
        "email": "avantika@radiantinfonet.com",
        "password": "Test@123"
    }
    response_data = requests.post(url=url1, headers=headers, json=payload)

    print("Response Text:", response_data)
    assert response_data.status_code == 400
