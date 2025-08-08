from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://preprod.testaonline.com/signin"

        # Locators
        self.email_field = (By.NAME, "email")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[normalize-space()='Login']")
        self.toast_message = (By.CLASS_NAME, "Toastify")
        self.welcome_text = (By.XPATH, "//h1[contains(text(), 'Team!👋')]")
        self.Incorrect_validation = (By.CLASS_NAME, "error-text")

    def open(self):
        self.driver.get(self.url)

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.email_field))
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def submit(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.submit()

    def get_toast_message(self):
        """Waits for toast and returns its text"""
        try:
            toast = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.toast_message)
            )
            return toast.text
        except:
            return None

    def is_logged_in(self):
        """Returns True if welcome text is found"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.welcome_text)
            )
            return True
        except:
            return False

    def get_Incorrect_validation(self):
        """Returns visible login error message text"""
        try:
            error = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.Incorrect_validation)
            )
            return error.text
        except:
            return None