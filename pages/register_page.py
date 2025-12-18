from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class RegisterPage:
    
    # Locators
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    CONFIRM_PASSWORD_FIELD = (By.ID, "confirmPassword")
    PID_FIELD = (By.ID, "pid")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Register']")
    
    # Message locators
    MESSAGE_SUCCESS = (By.XPATH, "//p[normalize-space()]")
    MESSAGE_ERROR = (By.CSS_SELECTOR, ".message.error")
    LABEL_EMAIL_ERROR = (By.CSS_SELECTOR, "label.validation-error[for='email']")
    LABEL_PASSWORD_ERROR = (By.CSS_SELECTOR, "label.validation-error[for='password']")
    LABEL_PID_ERROR = (By.CSS_SELECTOR, "label.validation-error[for='pid']")
    LABEL_CONFIRM_PASSWORD_ERROR = (By.CSS_SELECTOR, "label.validation-error[for='confirmPassword']")
    LOGIN_LINK_TEXT = (By.LINK_TEXT, "Login")
    CONFIRM_LINK_TEXT = (By.LINK_TEXT, "here")
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def enter_email(self, email: str):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        
    
    def enter_password(self, password: str):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
    
    def enter_confirm_password(self, confirm_password: str):
        self.driver.find_element(*self.CONFIRM_PASSWORD_FIELD).send_keys(confirm_password)
    
    def enter_pid(self, pid: str):
        self.driver.find_element(*self.PID_FIELD).send_keys(pid)
    
    def click_register(self):
        reg_btn = self.driver.find_element(*self.REGISTER_BUTTON)
        # Scroll this element into view before click it
        self.driver.execute_script('arguments[0].scrollIntoView();', reg_btn)
        reg_btn.click()
    
    def register(self, email: str, password: str, confirm_password: str, pid: str):
        """Complete registration in one method"""
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.enter_pid(pid)
        self.click_register()
    
    def get_success_message(self) -> str:
        return self.driver.find_element(*self.MESSAGE_SUCCESS).text.strip()
    
    def get_error_message(self) -> str:
        return self.driver.find_element(*self.MESSAGE_ERROR).text.strip()
    
    def get_label_email_error(self) -> str:
        return self.driver.find_element(*self.LABEL_EMAIL_ERROR).text.strip()

    def get_label_password_error(self) -> str:
        return self.driver.find_element(*self.LABEL_PASSWORD_ERROR).text.strip()

    def get_label_pid_error(self) -> str:
        return self.driver.find_element(*self.LABEL_PID_ERROR).text.strip()
    
    def get_label_confirm_password_error(self) -> str:
        return self.driver.find_element(*self.LABEL_CONFIRM_PASSWORD_ERROR).text.strip()
    
    def get_password_field_type(self) -> str:
        return self.driver.find_element(*self.PASSWORD_FIELD).get_attribute("type")
    
    def get_confirm_password_field_type(self) -> str:
        return self.driver.find_element(*self.CONFIRM_PASSWORD_FIELD).get_attribute("type")
    
    def get_register_button(self):
        return self.driver.find_element(*self.REGISTER_BUTTON)
    
    def nav_login_link(self):
        # Test Login link
        login_link = self.driver.find_element(*self.LOGIN_LINK_TEXT)
        login_link.click()
    
    def nav_confirm_link(self):
        confirm_link = self.driver.find_element(*self.CONFIRM_LINK_TEXT)
        confirm_link.click()