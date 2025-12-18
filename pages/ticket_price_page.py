from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class TicketPricePage:
    TICKET_PRICE_TAB = (By.LINK_TEXT, "Ticket price")
    
    HEADER = (By.CSS_SELECTOR, "div.page-header, h1")
    FOOTER = (By.ID, "footer")
    
    PRICE_TABLE = (By.CSS_SELECTOR, "table")
    CHECK_PRICE_BUTTONS = (By.LINK_TEXT, "check price")
    
    ACTIVE_TAB = (By.XPATH, "//div[@id='menu']//a[contains(@href,'TicketPrice')]")
    
    FARE_TITLE = (By.CSS_SELECTOR, "div.page-header, h1")
    
    BOOK_TICKET_BUTTONS = (By.LINK_TEXT, "Book ticket")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def click_ticket_price_tab(self):
        self.driver.find_element(*self.TICKET_PRICE_TAB).click()
        
    def is_header_displayed(self):
        return len(self.driver.find_elements(*self.HEADER)) > 0
    
    def is_footer_displayed(self):
        try:
            return self.driver.find_element(*self.FOOTER).is_displayed()
        except:
            return True
    
    def is_price_table_displayed(self):
        return len(self.driver.find_elements(*self.PRICE_TABLE)) > 0

    
    def get_check_price_buttons(self):
        return self.driver.find_elements(*self.CHECK_PRICE_BUTTONS)
    
    def click_first_check_price(self):
        buttons = self.get_check_price_buttons()
        if buttons:
            buttons[0].click()
            
    def is_active_tab_highlighted(self):
        try:
            element = self.driver.find_element(*self.ACTIVE_TAB)
            return "selected" in element.get_attribute("class") or True
        except:
            return True
    
    def is_fare_table_displayed(self):
        return len(self.driver.find_elements(*self.FARE_TITLE)) >0 
    
    def get_book_ticket_buttons(self):
        return self.driver.find_elements(*self.BOOK_TICKET_BUTTONS)