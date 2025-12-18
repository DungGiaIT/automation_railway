from selenium import webdriver
from selenium.webdriver.common.by import By
from base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import uuid

class TestRegister(BaseTest):
    ### chưa fix
    def test_reg_001_ui_display_correctly(self):
        """REG-001: UI of Register page display correctly"""
        self.home_page.go_to_register_page()
        self.assertIn("/Account/Register.cshtml", self.driver.current_url)
        img = self.driver.find_elements(By.TAG_NAME, "img")
        self.assertNotEqual(img.get_attribute("naturalWidth"), "0", f"Broken image found: {img.get_attribute('src')}")

    def test_reg_002_valid_registration_length(self):
        """REG-002: User can register with valid info - minimum length"""
        self.home_page.go_to_register_page()
        
        # Generate unique email with 6 characters (minimum)
        unique_part = uuid.uuid4().hex[:6]
        email = f"test{unique_part}@gmail.com"
        self.register_page.enter_email(email)
        self.register_page.enter_password("12345678")  # 8 chars (minimum)
        self.register_page.enter_confirm_password("12345678")
        self.register_page.enter_pid("12345678")  # 8 chars (minimum)
        self.register_page.click_register()
        # Verify success message
        success_msg = self.register_page.get_success_message()
        self.assertIn("you're here", success_msg.lower())

        """REG-002: User can register with valid info - maximum length"""
        self.home_page.go_to_register_page()

        unique_part = uuid.uuid4().hex[:18]
        email = f"test{unique_part}@gmail.com"
        
        self.register_page.enter_email(email)
        self.register_page.enter_password("a" * 64)  # 64 chars (maximum)
        self.register_page.enter_confirm_password("a" * 64)
        self.register_page.enter_pid("1" * 20)  # 20 chars (maximum)
        self.register_page.click_register()
        
        success_msg = self.register_page.get_success_message()
        self.assertIn("you're here", success_msg.lower())

    def test_reg_003_existed_email(self):
        self.home_page.go_to_register_page()
        
        # Generate unique email with 6 characters (minimum)
        unique_part = uuid.uuid4().hex[:6]
        email = f"test{unique_part}@gmail.com"
        self.register_page.enter_email(email)
        self.register_page.enter_password("12345678")  # 8 chars (minimum)
        self.register_page.enter_confirm_password("12345678")
        self.register_page.enter_pid("12345678")  # 8 chars (minimum)
        self.register_page.click_register()
        # Verify success message
        success_msg = self.register_page.get_success_message()
        self.assertIn("you're here", success_msg.lower())
        """REG-003: Error message when registering with existed email"""
        self.home_page.go_to_register_page()
        
        # Use known existing email
        self.register_page.enter_email(email)
        self.register_page.enter_password("12345678")
        self.register_page.enter_confirm_password("12345678")
        self.register_page.enter_pid("12345678")
        self.register_page.click_register()
        
        error_msg = self.register_page.get_error_message()
        self.assertIn("this email address is already in use.", error_msg.lower())

    def test_reg_004_empty_email(self):
        """REG-004: Error message when email is empty"""
        self.home_page.go_to_register_page()

        self.register_page.enter_password("12345678")
        self.register_page.enter_confirm_password("12345678")
        self.register_page.enter_pid("12345678")
        self.register_page.click_register()
        
        error_msg = self.register_page.get_error_message()
        error_label = self.register_page.get_label_email_error()
        self.assertIn("there're errors in the form. please correct the errors and try again.", error_msg.lower())
        self.assertIn("invalid email length", error_label.lower())

    def test_reg_005_invalid_email_format(self):
        """REG-005: User can't register with invalid email format"""
        self.home_page.go_to_register_page()
        
        self.register_page.enter_email("dung12345")  # Missing @ and domain
        self.register_page.enter_password("12345678")
        self.register_page.enter_confirm_password("12345678")
        self.register_page.enter_pid("12345678")
        self.register_page.click_register()
        
        error_msg = self.register_page.get_error_message()
        error_label = self.register_page.get_label_email_error()
        self.assertIn("there're errors in the form. please correct the errors and try again.", error_msg.lower())
        self.assertIn("invalid email address", error_label.lower())

    def test_reg_006_email_with_special_chars(self):
        """REG-006: User can't register with special characters in email"""
        self.home_page.go_to_register_page()
        self.register_page.register("dung@-gmail.com", "12345678", "12345678", "12345678")
        error_msg = self.register_page.get_error_message()
        error_email_label = self.register_page.get_label_email_error()
        self.assertIn("there're errors in the form. please correct the errors and try again.", error_msg.lower())
        self.assertIn("invalid email address", error_email_label.lower())

    def test_reg_007_invalid_registration_length(self):
        """REG-007: User can't register with email shorter than 6 characters"""
        self.home_page.go_to_register_page()
        unique_part = uuid.uuid4().hex[:1]
        email = f"{unique_part}@g.c"
        
        self.register_page.enter_email(email)
        self.register_page.enter_password("1234567")
        self.register_page.enter_confirm_password("1234567")
        self.register_page.enter_pid("1234567")
        self.register_page.click_register()
        
        error_msg = self.register_page.get_error_message()
        error_label_email = self.register_page.get_label_email_error()
        error_label_password = self.register_page.get_label_password_error()
        error_label_pid = self.register_page.get_label_pid_error()
        self.assertIn("there're errors in the form. please correct the errors and try again.", error_msg.lower())
        self.assertIn("invalid email length", error_label_email.lower())
        self.assertIn("invalid password length", error_label_password.lower())
        self.assertIn("invalid id length", error_label_pid.lower())

        unique_part = uuid.uuid4().hex[:19]
        email = f"test{unique_part}@gmail.com"# 33 characters
        
        self.register_page.enter_email(email)
        self.register_page.enter_password("1"*65)# 65 characters
        self.register_page.enter_confirm_password("1"*65)
        self.register_page.enter_pid("1"*21)# 21 characters
        self.register_page.click_register()
        
        error_msg = self.register_page.get_error_message()
        error_label_email = self.register_page.get_label_email_error()
        error_label_password = self.register_page.get_label_password_error()
        error_label_pid = self.register_page.get_label_pid_error()
        self.assertIn("there're errors in the form. please correct the errors and try again.", error_msg.lower())
        self.assertIn("invalid email length", error_label_email.lower())
        self.assertIn("invalid password length", error_label_password.lower())
        self.assertIn("invalid id length", error_label_pid.lower())

    def test_reg_009_password_mismatch(self):
        """REG-009: User can't register when confirm password doesn't match"""
        self.home_page.go_to_register_page()
        
        unique_part = uuid.uuid4().hex[:6]
        email = f"test{unique_part}@gmail.com"
        
        self.register_page.enter_email(email)
        self.register_page.enter_password("12345678")
        self.register_page.enter_confirm_password("12345679")  # Different
        self.register_page.enter_pid("12345678")
        self.register_page.click_register()
        
        error_msg = self.register_page.get_error_message()
        error_label_confirm = self.register_page.get_label_confirm_password_error()
        self.assertIn("there're errors in the form. please correct the errors and try again.", error_msg.lower())
        self.assertIn("the two passwords do not match", error_label_confirm.lower())

    def test_reg_011_invalid_pid_special_chars(self):
        """REG-011: User can't register with invalid PID (special characters)"""
        self.home_page.go_to_register_page()
        
        timestamp = str(int(time.time()))
        email = f"test{timestamp}@gmail.com"
        
        self.register_page.enter_email(email)
        self.register_page.enter_password("12345678")
        self.register_page.enter_confirm_password("12345678")
        self.register_page.enter_pid("12122#@2232")  # Special characters
        self.register_page.click_register()
        
        error_msg = self.register_page.get_error_message()
        error_label = self.register_page.get_label_pid_error_error()
        self.assertIn("there're errors in the form. please correct the errors and try again.", error_msg.lower())
        self.assertIn("invalid id form", error_label.lower())

    def test_reg_012_all_fields_empty(self):
        """REG-012: User can't register with all fields empty"""
        self.home_page.go_to_register_page()
        
        self.register_page.click_register()
        
        error_msg = self.register_page.get_error_message()
        error_email_label = self.register_page.get_label_email_error()
        error_password_label = self.register_page.get_label_password_error()
        error_pid_label = self.register_page.get_label_pid_error()
        self.assertIn("there're errors in the form. please correct the errors and try again.", error_msg.lower())
        self.assertIn("invalid email length", error_email_label.lower())
        self.assertIn("invalid password length", error_password_label.lower())
        self.assertIn("invalid id length", error_pid_label.lower())
        

    def test_reg_014_password_encrypted(self):
        """REG-014: Password is displayed in encrypted form"""
        self.home_page.go_to_register_page()
        
        password_type = self.register_page.get_password_field_type()
        self.assertEqual(password_type, "password", 
                        "Password field should be type='password'")
        
        confirm_password_type = self.register_page.get_confirm_password_field_type()
        self.assertEqual(confirm_password_type, "password", 
                        "Confirm password field should be type='password'")

    # def test_reg_015_hover_color_change(self):
    #     """REG-015: The hovering operation changes the color of links and button"""
    #     self.home_page.go_to_register_page()
        
    #     register_button = self.register_page.get_register_button()
    #     before_color = register_button.value_of_css_property('background-color')
        
    #     # Hover over button
    #     from selenium.webdriver.common.action_chains import ActionChains
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(register_button).perform()
    #     time.sleep(0.5)
        
    #     after_color = register_button.value_of_css_property('background-color')

    #     self.assertTrue(register_button.is_displayed())

    def test_reg_016_navigation_links(self):
        """REG-016: User can navigate to corresponding pages when clicking on links"""
        self.home_page.go_to_register_page()
        self.register_page.nav_login_link()
        self.assertIn("/Account/Login.cshtml", self.driver.current_url)
        
        self.home_page.go_to_register_page()
        self.register_page.nav_confirm_link()
        self.assertIn("/Account/Confirm.cshtml", self.driver.current_url)