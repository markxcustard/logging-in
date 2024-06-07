import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging_in.config.settings import USERNAME, PASSWORD, URL, INCORRECT_PASSWORD
from logging_in.pages.login_page import LoginPage

@pytest.fixture(scope="function", params=["firefox", "chrome", "safari"])
def driver(request):
    browser = request.param
    if browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--private")
        driver = webdriver.Firefox(options=options)
    elif browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
    elif browser == 'safari':
        options = webdriver.SafariOptions()
        driver = webdriver.Safari(options=options)
    else:
        raise ValueError("Unrecognized browser type: {}".format(browser))

    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield driver

    # Ensure browser is closed after the test
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        driver.save_screenshot(f"screenshot_{browser}.png")
    driver.quit()

@pytest.mark.usefixtures("driver")
class TestLogin:

    @pytest.mark.parametrize("username,password,expected", [
        (USERNAME, PASSWORD, "feed"),  # Positive test case
        (USERNAME, INCORRECT_PASSWORD, "error")  # Negative test case
    ])
    def test_login(self, username, password, expected):
        login_page = LoginPage(self.driver)
        login_page.visit(URL)

        # Explicit waits for elements
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, 'username'))
        )
        login_page.enter_username(username)

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, 'password'))
        )
        login_page.enter_password(password)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and contains(@class, "btn__primary--large")]'))
        )
        login_page.click_login()

        if expected == "feed":
            # Wait for the URL to change for a successful login
            WebDriverWait(self.driver, 20).until(
                EC.url_contains(expected)
            )
            assert expected in self.driver.current_url
        else:
            # Check for error message for an unsuccessful login
            error_message = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, 'error-for-password'))
            )
            assert error_message.is_displayed()

if __name__ == "__main__":
    pytest.main()
