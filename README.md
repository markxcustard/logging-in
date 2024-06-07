# Logging In Automation

This project automates the login process for a web application using Selenium. It supports running tests on Firefox, Chrome, and Safari. The project is set up with a Page Object Model (POM) structure and uses environment variables to securely manage credentials.


## Setup

### Prerequisites

- Python 3.6+
- Selenium
- Browser drivers for Firefox, Chrome, and Safari
- `python-dotenv` for managing environment variables

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/markxcustard/logging-in.git
    cd logging_in
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables:

    Create a `.env` file in the root directory of the project:

    ```dotenv
    USERNAME=your_username
    PASSWORD=your_password
    INCORRECT_PASSWORD=incorrect_password
    ```

### Browser Drivers

Ensure you have the appropriate browser drivers installed and accessible in your PATH. For example:

- [GeckoDriver for Firefox](https://github.com/mozilla/geckodriver/releases)
- [ChromeDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [SafariDriver for Safari](https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari)

## Running Tests

To run the tests, use `pytest`:

```bash
pytest logging_in/tests --tb=short --maxfail=1


Project Details
config/settings.py
Manages the environment variables and settings for the project.

pages/base_page.py
Defines the base page class that all other page objects inherit from.

pages/login_page.py
Defines the login page object, including methods for interacting with the login page.

tests/test_login.py
Contains the tests for logging in, including positive and negative test cases.
