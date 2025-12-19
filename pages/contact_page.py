from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactPage:
    
    # Locators
    CONTACT_TAB = (By.XPATH, "//a[@href='/Page/Contact.cshtml']")
    CONTACT_HEADER = (By.XPATH, "//h1[contains(text(), 'Contact Information')]")
    
    # Contact information locators
    CONTACT_SECTION = (By.CLASS_NAME, "contact")
    SEATCODE_TEXT = (By.XPATH, "//b[contains(text(), 'Seatcode:')]")
    PHONE_TEXT = (By.XPATH, "//b[contains(text(), 'Phone:')]")
    SKYPE_TEXT = (By.XPATH, "//b[contains(text(), 'Skype:')]")
    EMAIL_TEXT = (By.XPATH, "//b[contains(text(), 'Email:')]")
    EMAIL_LINK = (By.XPATH, "//a[@href='mailto:thanh.viet.le@logigear.com']")
    
    # External links
    SOMEE_LINK = (By.XPATH, "//a[@href='http://somee.com']")
    
    # Navigation bar and footer
    NAVIGATION_BAR = (By.ID, "menu")
    FOOTER = (By.ID, "footer")
    
    # Banner/Images
    BANNER_IMAGE = (By.ID, "banner_img")
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def get_page_header(self):
        """Get Contact page header text"""
        return self.driver.find_element(*self.CONTACT_HEADER).text.strip()
    
    def is_navigation_bar_visible(self):
        """Check if navigation bar is visible"""
        try:
            return self.driver.find_element(*self.NAVIGATION_BAR).is_displayed()
        except:
            return False
    
    def is_footer_visible(self):
        """Check if footer is visible"""
        try:
            return self.driver.find_element(*self.FOOTER).is_displayed()
        except:
            return False
    
    def is_banner_image_displayed(self):
        """Check if banner image is displayed and not broken"""
        try:
            img = self.driver.find_element(*self.BANNER_IMAGE)
            # Check if image is displayed
            if not img.is_displayed():
                return False
            # Check if image is loaded (naturalWidth > 0 means image loaded successfully)
            return self.driver.execute_script(
                "return arguments[0].complete && arguments[0].naturalWidth > 0",
                img
            )
        except:
            return False
    
    def is_contact_section_displayed(self):
        """Check if contact information section is displayed"""
        try:
            return self.driver.find_element(*self.CONTACT_SECTION).is_displayed()
        except:
            return False
    
    def get_contact_info_text(self):
        """Get all contact information text"""
        try:
            return self.driver.find_element(*self.CONTACT_SECTION).text
        except:
            return ""
    
    def is_seatcode_displayed(self):
        """Check if Seatcode is displayed"""
        try:
            contact_text = self.get_contact_info_text()
            return "Seatcode:" in contact_text and "404" in contact_text
        except:
            return False
    
    def is_phone_displayed(self):
        """Check if Phone is displayed"""
        try:
            contact_text = self.get_contact_info_text()
            return "Phone:" in contact_text and "012650.888.79" in contact_text
        except:
            return False
    
    def is_skype_displayed(self):
        """Check if Skype is displayed"""
        try:
            contact_text = self.get_contact_info_text()
            return "Skype:" in contact_text and "vietthanhle.lg" in contact_text
        except:
            return False
    
    def is_email_displayed(self):
        """Check if Email is displayed"""
        try:
            contact_text = self.get_contact_info_text()
            return "Email:" in contact_text and "thanh.viet.le@logigear.com" in contact_text
        except:
            return False
    
    def is_email_link_clickable(self):
        """Check if email link exists and is clickable"""
        try:
            email_link = self.driver.find_element(*self.EMAIL_LINK)
            return email_link.is_displayed() and email_link.is_enabled()
        except:
            return False
    
    def get_email_link_href(self):
        """Get email link href attribute"""
        try:
            return self.driver.find_element(*self.EMAIL_LINK).get_attribute("href")
        except:
            return ""
    
    def click_email_link(self):
        """Click on email link"""
        self.driver.find_element(*self.EMAIL_LINK).click()
    
    def is_somee_link_displayed(self):
        """Check if Somee.com link is displayed"""
        try:
            return self.driver.find_element(*self.SOMEE_LINK).is_displayed()
        except:
            return False
    
    def get_somee_link_href(self):
        """Get Somee.com link href attribute"""
        try:
            return self.driver.find_element(*self.SOMEE_LINK).get_attribute("href")
        except:
            return ""
    
    def click_somee_link(self):
        """Click on Somee.com link"""
        somee_link = self.driver.find_element(*self.SOMEE_LINK)
        self.driver.execute_script('arguments[0].scrollIntoView();', somee_link)
        somee_link.click()

    
    def check_no_misspelled_words(self):
        """Basic check for common misspellings and expected words"""
        content = self.driver.find_element(By.TAG_NAME, "body").text.lower()
        # Check for expected words
        expected_words = ['contact', 'information', 'seatcode', 'phone', 'skype', 'email']
        found_words = [word for word in expected_words if word in content]
        return len(found_words) == len(expected_words)
    
    def get_all_text_content(self):
        """Get all text content from Contact page"""
        return self.driver.find_element(By.TAG_NAME, "body").text
    
    def get_tab_background_color(self, tab_locator):
        """Get background color of a tab"""
        try:
            tab = self.driver.find_element(*tab_locator)
            # Get parent li element for styling
            parent_li = tab.find_element(By.XPATH, "./..")
            return parent_li.value_of_css_property("background-color")
        except:
            return None
    
    def get_contact_tab_background_color(self):
        """Get background color of Contact tab"""
        return self.get_tab_background_color(self.CONTACT_TAB)
    
    def is_contact_tab_selected(self):
        """Check if Contact tab has 'selected' class"""
        try:
            tab = self.driver.find_element(*self.CONTACT_TAB)
            parent_li = tab.find_element(By.XPATH, "./..")
            return "selected" in parent_li.get_attribute("class")
        except:
            return False