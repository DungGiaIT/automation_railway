from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from base_test import BaseTest
import time


class TestContact(BaseTest):
    
    def test_Cont_001(self):
        self.home_page.go_to_contact_page()
        
        # Verify Contact page is displayed
        self.assertIn("/Page/Contact.cshtml", self.driver.current_url)
        
        # Verify Contact header is displayed
        header = self.contact_page.get_page_header()
        self.assertEqual(
            header,
            "Contact Information",
            "Contact header is not displayed correctly"
        )
        
        # Verify navigation bar is visible
        self.assertTrue(
            self.contact_page.is_navigation_bar_visible(),
            "Navigation bar is not visible"
        )
        
        # Verify footer is visible
        self.assertTrue(
            self.contact_page.is_footer_visible(),
            "Footer is not visible"
        )
        
        # Check for no broken images
        self.assertTrue(
            self.contact_page.is_banner_image_displayed(),
            "Banner image is broken or not displayed"
        )
        
        # Check for no misspelled words
        self.assertTrue(
            self.contact_page.check_no_misspelled_words(),
            "Some expected words are missing or misspelled on Contact page"
        )
        
        # Verify Contact tab is selected (has different color)
        self.assertTrue(
            self.contact_page.is_contact_tab_selected(),
            "Contact tab is not marked as selected"
        )
        
        # Verify contact information section is displayed
        self.assertTrue(
            self.contact_page.is_contact_section_displayed(),
            "Contact information section is not displayed"
        )
        
        # Verify Seatcode is displayed
        self.assertTrue(
            self.contact_page.is_seatcode_displayed(),
            "Seatcode is not displayed correctly"
        )
        
        # Verify Phone is displayed
        self.assertTrue(
            self.contact_page.is_phone_displayed(),
            "Phone is not displayed correctly"
        )
        
        # Verify Skype is displayed
        self.assertTrue(
            self.contact_page.is_skype_displayed(),
            "Skype is not displayed correctly"
        )
        
        # Verify Email is displayed
        self.assertTrue(
            self.contact_page.is_email_displayed(),
            "Email is not displayed correctly"
        )
        
        # Verify email link is clickable
        self.assertTrue(
            self.contact_page.is_email_link_clickable(),
            "Email link is not clickable"
        )
        
        # Verify email link href
        email_href = self.contact_page.get_email_link_href()
        self.assertEqual(
            email_href,
            "mailto:thanh.viet.le@logigear.com",
            f"Email link href is incorrect. Expected 'mailto:thanh.viet.le@logigear.com', got '{email_href}'"
        )
    
    def test_Cont_002(self):
        self.home_page.go_to_contact_page()
        
        # Verify we're on Contact page
        self.assertIn("/Page/Contact.cshtml", self.driver.current_url)
        
        # Store the original window handle
        original_window = self.driver.current_window_handle
        
        self.assertTrue(
            self.contact_page.is_somee_link_displayed(),
            "Somee.com link is not displayed"
        )
        
        somee_href = self.contact_page.get_somee_link_href()
        
        self.assertEqual(
            somee_href.rstrip("/"),
            "http://somee.com",
            f"Somee link href is incorrect. Expected 'http://somee.com', got '{somee_href}'"
        )

        self.contact_page.click_somee_link()
        time.sleep(1)
        
        # Wait for new window/tab and switch to it
        # The link might open in same window or new window/tab
        all_windows = self.driver.window_handles
        if len(all_windows) > 1:
            # New window/tab opened
            for window in all_windows:
                if window != original_window:
                    self.driver.switch_to.window(window)
                    break
        
        # Verify navigation to Somee.com
        time.sleep(1)
        current_url = self.driver.current_url.lower()
        self.assertTrue(
            "somee.com" in current_url,
            f"Did not navigate to Somee.com. Current URL: {current_url}"
        )
        
        # Close new window if opened and switch back to original
        if len(all_windows) > 1:
            self.driver.close()
            self.driver.switch_to.window(original_window)
        else:
            # Navigate back if opened in same window
            self.driver.back()
            time.sleep(1)
        
        # Go back to Contact page to test email link
        self.home_page.go_to_contact_page()
        time.sleep(1)
        # Test 2: Email link
        # Verify email link is displayed and clickable
        self.assertTrue(
            self.contact_page.is_email_link_clickable(),
            "Email link is not clickable"
        )
        
        # Verify email link href contains mailto protocol
        email_href = self.contact_page.get_email_link_href()
        self.assertEqual(
            email_href,
            "mailto:thanh.viet.le@logigear.com",
            f"Email link href is incorrect. Expected 'mailto:thanh.viet.le@logigear.com', got '{email_href}'"
        )
        
        # Note: We don't click the email link as it would try to open email client
        # The href verification is sufficient to confirm the link works correctly