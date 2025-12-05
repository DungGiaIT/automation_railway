from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.faq_page import FAQPage
from pages.contact_page import ContactPage
from pages.time_table_page import TimeTablePage
from pages.ticket_price_page import TicketPricePage
from pages.book_ticket_page import BookTicketPage
from pages.register_page import RegisterPage

class HomePage:

    NAV_BAR_LOGIN_LOCATOR = (By.LINK_TEXT, 'Login')
    NAV_BAR_HOME_LOCATOR = (By.LINK_TEXT, 'Home')
    NAV_BAR_FAQ_LOCATOR = (By.LINK_TEXT, 'FAQ')
    NAV_BAR_CONTACT_LOCATOR = (By.LINK_TEXT, 'Contact')
    NAV_BAR_TIMETABLE_LOCATOR = (By.LINK_TEXT, 'Timetable')
    NAV_BAR_TICKET_PRICE_LOCATOR = (By.LINK_TEXT, 'Ticket price')
    NAV_BAR_BOOK_TICKET_LOCATOR = (By.LINK_TEXT, 'Book ticket')
    NAV_BAR_REGISTER_LOCATOR = (By.LINK_TEXT, 'Register')
    NAV_BAR_CREATE_ACCOUNT_LOCATOR = (By.LINK_TEXT, 'create an account')
    WELCOME_MSG_LOCATOR = (By.CSS_SELECTOR, 'div.account strong')
    
    def __init__(self, webdriver: WebDriver):
        self.driver = webdriver

    def go_to_login_page(self):
        self.driver.find_element(*self.NAV_BAR_LOGIN_LOCATOR).click()
        return LoginPage(self.driver)

    def go_to_home_page(self):
        self.driver.find_element(*self.NAV_BAR_HOME_LOCATOR).click()
        return self.driver

    def go_to_faq_page(self):
        self.driver.find_element(*self.NAV_BAR_FAQ_LOCATOR).click()
        return FAQPage(self.driver)

    def go_to_contact_page(self):
        self.driver.find_element(*self.NAV_BAR_CONTACT_LOCATOR).click()
        return  ContactPage(self.driver)

    def go_to_time_table_page(self):
        self.driver.find_element(*self.NAV_BAR_TIMETABLE_LOCATOR).click()
        return TimeTablePage(self.driver)

    def go_to_ticket_price_page(self):
        self.driver.find_element(*self.NAV_BAR_TICKET_PRICE_LOCATOR).click()
        return TicketPricePage(self.driver)

    def go_to_book_ticket_page(self):
        self.driver.find_element(*self.NAV_BAR_BOOK_TICKET_LOCATOR).click()
        return BookTicketPage(self.driver)

    def go_to_register_page(self):
        self.driver.find_element(*self.NAV_BAR_REGISTER_LOCATOR).click()
        return RegisterPage(self.driver)

    def go_to_create_account(self):
        self.driver.find_element(*self.NAV_BAR_CREATE_ACCOUNT_LOCATOR).click()
        return RegisterPage(self.driver)

    def get_welcome_msg(self) -> str:
        return self.driver.find_element(*self.WELCOME_MSG_LOCATOR).text