from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ForgotPasswordPage:

    EMAIL_FIELD = (By.ID, "email")
    SEND_INSTRUCTIONS_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Send Instructions']")

    # Nếu trang có message sau khi gửi → bạn có thể thêm:
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, ".message.success")    # tuỳ UI
    MESSAGE_ERROR = (By.CSS_SELECTOR, ".message.error")        # tuỳ UI


    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_email(self, email: str):
        field = self.driver.find_element(*self.EMAIL_FIELD)
        field.clear()
        field.send_keys(email)

    def click_send_instructions(self):
        self.driver.find_element(*self.SEND_INSTRUCTIONS_BUTTON).click()

    # Tuỳ chọn:
    def get_success_message(self):
        return self.driver.find_element(*self.MESSAGE_SUCCESS).text


    def get_error_message(self):
        return self.driver.find_element(*self.MESSAGE_ERROR).text
