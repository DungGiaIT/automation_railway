from selenium import webdriver
from selenium.webdriver.common.by import By
from base_test import BaseTest

class TestHome(BaseTest):
    def test_nav(self):
        self.home_page.go_to_faq_page()
        self.home_page.go_to_home_page()
        self.home_page.go_to_create_account()
        self.home_page.go_to_contact_page()
        self.home_page.go_to_ticket_price_page()
        self.home_page.go_to_time_table_page()
        self.home_page.go_to_book_ticket_page()
        self.home_page.go_to_register_page()
        self.home_page.go_to_login_page()
        