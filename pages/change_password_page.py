from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ChangePasswordPage():
    

    def __init__(self, driver:WebDriver):
        self.driver = driver