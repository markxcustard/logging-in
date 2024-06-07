from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, 'username')  # LinkedIn uses 'username' for the email field
    PASSWORD_INPUT = (By.ID, 'password')  # LinkedIn uses 'password' for the password field
    LOGIN_BUTTON = (By.XPATH, '//button[contains(@class, "btn__primary--large")]')

    def enter_username(self, username):
        self.find_element(*self.EMAIL_INPUT).send_keys(username)

    def enter_password(self, password):
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.find_element(*self.LOGIN_BUTTON).click()
