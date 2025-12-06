from selenium import webdriver
from selenium.webdriver.common.by import By
from base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHome(BaseTest):

    def test_hom_001(self):
        expected_texts = ["Home", "FAQ", "Contact", "Timetable", "Ticket price", "Book ticket", "Register", "Login"]

        locators = [
            self.home_page.NAV_BAR_HOME_LOCATOR,
            self.home_page.NAV_BAR_FAQ_LOCATOR,
            self.home_page.NAV_BAR_CONTACT_LOCATOR,
            self.home_page.NAV_BAR_TIMETABLE_LOCATOR,
            self.home_page.NAV_BAR_TICKET_PRICE_LOCATOR,
            self.home_page.NAV_BAR_BOOK_TICKET_LOCATOR,
            self.home_page.NAV_BAR_REGISTER_LOCATOR,
            self.home_page.NAV_BAR_LOGIN_LOCATOR
        ]

        for locator, expected_text in zip(locators, expected_texts):
            element_text = self.driver.find_element(*locator).text
            self.assertEqual(element_text, expected_text)

    def test_hom_002(self):
        self.home_page.go_to_home_page()
        self.assertIn("/Page/HomePage.cshtml", self.driver.current_url)

        self.home_page.go_to_create_account()
        self.assertIn("/Account/Register.cshtml", self.driver.current_url)

        self.home_page.go_to_contact_page()
        self.assertIn("/Page/Contact.cshtml", self.driver.current_url)

        self.home_page.go_to_ticket_price_page()
        self.assertIn("/Page/TrainPriceListPage.cshtml", self.driver.current_url)

        self.home_page.go_to_time_table_page()
        self.assertIn("/Page/TrainTimeListPage.cshtml", self.driver.current_url)

        self.home_page.go_to_book_ticket_page()
        self.assertIn("/Account/Login.cshtml?ReturnUrl=/Page/BookTicketPage.cshtml", self.driver.current_url)

        self.home_page.go_to_register_page()
        self.assertIn("/Account/Register.cshtml", self.driver.current_url)

        self.home_page.go_to_login_page()
        self.assertIn("/Account/Login.cshtml", self.driver.current_url)

        # self.home_page.go_to_faq_page()
        # self.assertIn("/Page/FAQ.cshtml", self.driver.current_url)

    def test_hom_003(self):
        self.home_page.go_to_login_page()

        self.login_page.login('cijnuj@ramcloud.us', '123456789')
        self.assertEqual(self.home_page.get_welcome_msg(), 'Welcome cijnuj@ramcloud.us')

        self.home_page.go_to_home_page()
        self.assertIn("/Page/HomePage.cshtml", self.driver.current_url)

        self.home_page.go_to_contact_page()
        self.assertIn("/Page/Contact.cshtml", self.driver.current_url)

        self.home_page.go_to_ticket_price_page()
        self.assertIn("/Page/TrainPriceListPage.cshtml", self.driver.current_url)

        self.home_page.go_to_time_table_page()
        self.assertIn("/Page/TrainTimeListPage.cshtml", self.driver.current_url)

        self.home_page.go_to_book_ticket_page()
        self.assertIn("/Page/BookTicketPage.cshtml", self.driver.current_url)

        self.home_page.go_to_my_ticket_page()
        self.assertIn("/Page/ManageTicket.cshtml", self.driver.current_url)

        self.home_page.go_to_change_password_page()
        self.assertIn("/Account/ChangePassword.cshtml", self.driver.current_url)

        self.home_page.go_to_log_out()
        self.assertIn("/Page/HomePage.cshtml", self.driver.current_url)

    # def test_hom_005_tab_highlight_change(self):
    #     tabs = [
    #         # self.home_page.NAV_BAR_FAQ_LOCATOR,
    #         self.home_page.NAV_BAR_CONTACT_LOCATOR,
    #         self.home_page.NAV_BAR_HOME_LOCATOR,
    #         self.home_page.NAV_BAR_TIMETABLE_LOCATOR,
    #         self.home_page.NAV_BAR_TICKET_PRICE_LOCATOR,
    #         self.home_page.NAV_BAR_BOOK_TICKET_LOCATOR,
    #         self.home_page.NAV_BAR_REGISTER_LOCATOR,
    #         self.home_page.NAV_BAR_LOGIN_LOCATOR
    #     ]

    #     # Lấy màu hiện tại
    #     for tab in tabs:
    #         element = self.driver.find_element(*tab)
    #         before_color = element.value_of_css_property('color')

    #         element.click()

    #         # Đợi elemennt thay đổi UI
    #         WebDriverWait(self.driver, 5).until(
    #             EC.visibility_of_element_located(tab)
    #         )

    #         element_after = self.driver.find_element(*tab)
    #         after_color = element_after.value_of_css_property('color')

    #         # So sánh màu
    #         self.assertNotEqual(
    #             before_color,
    #             after_color,
    #             f"Expected highlight color change after selecting tab {element.text}"
    #         )

    # def test_no_broken_images(self):
    #     images = self.driver.find_elements(By.TAG_NAME, "img")
    #     for img in images:
    #         self.assertNotEqual(img.get_attribute("naturalWidth"), "0")

