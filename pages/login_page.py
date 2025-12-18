from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    EMAIL_TXT_LOCATOR = (By.ID, 'username')
    PASSWORD_TXT_LOCATOR = (By.NAME, 'password')
    LOGIN_BTN_LOCATOR = (By.CSS_SELECTOR, 'input[value=Login]')
    MESSAGE_ERROR_LOGIN_FORM = (By.CSS_SELECTOR, ".message.error.LoginForm")
    PASSWORD_FIELD = (By.ID, "password")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Forgot Password page']")

    # Constructor
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Actions
    def enter_email(self, email: str):
        self.driver.find_element(*self.EMAIL_TXT_LOCATOR).send_keys(email)

    def enter_password(self, password: str):
        self.driver.find_element(*self.PASSWORD_TXT_LOCATOR).send_keys(password)

    def click_login_btn(self):
        login_btn = self.driver.find_element(*self.LOGIN_BTN_LOCATOR)
        # Scroll this element into view before click it
        self.driver.execute_script('arguments[0].scrollIntoView();', login_btn)
        login_btn.click()

        # Waiting for the page to load after clicking the login button
        # Wait for the login_btn is disappear (or not display or invisibility)
       

    def login(self, username: str, password: str):
        self.enter_email(username)
        # 
        self.enter_password(password)
        self.click_login_btn()
        WebDriverWait(self.driver, 10).until(
            EC.any_of(
                EC.visibility_of_element_located(self.MESSAGE_ERROR_LOGIN_FORM),
                EC.invisibility_of_element_located(self.LOGIN_BTN_LOCATOR)
            )
    )

    def get_error_message(self):
        return self.driver.find_element(*self.MESSAGE_ERROR_LOGIN_FORM).text.strip()
    
    def get_password_type(self):
        return self.driver.find_element(*self.PASSWORD_FIELD).get_attribute("type")
    
    def click_forgot_password(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()