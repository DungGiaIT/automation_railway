from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.faq_page import FAQPage
from pages.contact_page import ContactPage
from pages.time_table_page import TimeTablePage
from pages.ticket_price_page import TicketPricePage
from pages.book_ticket_page import BookTicketPage
from pages.register_page import RegisterPage



class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.faq_page = FAQPage(self.driver)
        self.contact_page = ContactPage(self.driver)
        self.time_table_page = TimeTablePage(self.driver)
        self.ticket_price_page = TicketPricePage(self.driver)
        self.book_ticket_page = BookTicketPage(self.driver)
        self.register_page = RegisterPage(self.driver)

        self.driver.get('http://railwayb1.somee.com/')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()