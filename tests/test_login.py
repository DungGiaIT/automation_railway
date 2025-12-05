from selenium import webdriver
from selenium.webdriver.common.by import By
from base_test import BaseTest

class testLogin(BaseTest):
    def test_login(self):
        self.home_page.go_to_login_page()

        self.login_page.login('cijnuj@ramcloud.us', '123456789')

        self.assertEqual(self.home_page.get_welcome_msg(), 'Welcome cijnuj@ramcloud.us')
        
# if __name__ == '__main__':
#     unittest.main()