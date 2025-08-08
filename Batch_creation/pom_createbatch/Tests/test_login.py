from Pages.LoginPage import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("abhijeet@radiantinfonet.com", "Abhijeet@123")

    logintoast = login_page.get_toast_message()
    assert logintoast == "User login successfully", f"Expected toast not found. Got: {logintoast}"

def test_Invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("avantika@radiantinfonet.com", "Avantika@123")

    Incorrect_validation = login_page.get_Incorrect_validation()

    assert Incorrect_validation == "wrong password", f"Expected 'wrong password' but got: {Incorrect_validation}"
