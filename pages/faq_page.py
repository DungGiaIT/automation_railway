from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FAQPage:
    
    # Locators
    FAQ_TAB = (By.XPATH, "//a[@href='/Page/FAQ.cshtml']")
    FAQ_HEADER = (By.XPATH, "//h1[contains(text(), 'Frequently Asked Questions')]")
    
    # Questions locators (based on actual HTML structure)
    QUESTION_BOOK_TICKET = (By.XPATH, "//a[@href='#1']")  # How to book a ticket?
    QUESTION_EXPIRED = (By.XPATH, "//a[@href='#2']")  # Why do my tickets get expired?
    QUESTION_PAY = (By.XPATH, "//a[@href='#3']")  # How to pay for my tickets?
    QUESTION_HOW_MANY = (By.XPATH, "//a[@href='#4']")  # How many tickets can I book?
    QUESTION_FILTER = (By.XPATH, "//a[@href='#5']")  # Filter in My Ticket page
    QUESTION_CHANGE = (By.XPATH, "//a[@href='#6']")  # Change station/date
    QUESTION_BROWSER = (By.XPATH, "//a[@href='#7']")  # Browser support
    QUESTION_OTHER = (By.XPATH, "//a[@href='#8']")  # Other questions
    
    # Answer sections locators (IDs from HTML)
    ANSWER_BOOK_TICKET = (By.ID, "1")
    ANSWER_EXPIRED = (By.ID, "2")
    ANSWER_PAY = (By.ID, "3")
    ANSWER_HOW_MANY = (By.ID, "4")
    ANSWER_FILTER = (By.ID, "5")
    ANSWER_CHANGE = (By.ID, "6")
    ANSWER_BROWSER = (By.ID, "7")
    ANSWER_OTHER = (By.ID, "8")
    
    # Links in answers (from HTML)
    CREATE_ACCOUNT_LINK = (By.XPATH, "//a[@href='/Account/Register.cshtml']")
    BOOK_TICKET_PAGE_LINK = (By.XPATH, "//a[@href='/Page/BookTicketPage']")
    
    # Navigation bar and footer
    NAVIGATION_BAR = (By.ID, "menu")
    FOOTER = (By.ID, "footer")
    
    # Dictionary mapping question numbers to locators
    QUESTION_LOCATORS = {
        1: QUESTION_BOOK_TICKET,
        2: QUESTION_EXPIRED,
        3: QUESTION_PAY,
        4: QUESTION_HOW_MANY,
        5: QUESTION_FILTER,
        6: QUESTION_CHANGE,
        7: QUESTION_BROWSER,
        8: QUESTION_OTHER
    }
    
    ANSWER_LOCATORS = {
        1: ANSWER_BOOK_TICKET,
        2: ANSWER_EXPIRED,
        3: ANSWER_PAY,
        4: ANSWER_HOW_MANY,
        5: ANSWER_FILTER,
        6: ANSWER_CHANGE,
        7: ANSWER_BROWSER,
        8: ANSWER_OTHER
    }
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def get_page_header(self):
        """Get FAQ page header text"""
        return self.driver.find_element(*self.FAQ_HEADER).text.strip()
    
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
    
    def click_question(self, question_locator):
        """Click on a question link"""
        question = self.driver.find_element(*question_locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', question)
        question.click()
    
    def click_question_by_number(self, question_number):
        """Click on a question by its number (1-8)"""
        if question_number not in self.QUESTION_LOCATORS:
            raise ValueError(f"Invalid question number: {question_number}. Must be 1-8.")
        self.click_question(self.QUESTION_LOCATORS[question_number])
    
    def click_book_ticket_question(self, question_number=1):
        """Click on a specific question
        Args:
            question_number (int): Question number (1-8). Default is 1 (How to book a ticket?)
        """
        self.click_question_by_number(question_number)
    
    def click_expired_question(self):
        """Click on 'Why do my tickets get expired?' question"""
        self.click_question(self.QUESTION_EXPIRED)
    
    def click_pay_question(self):
        """Click on 'How to pay for my tickets?' question"""
        self.click_question(self.QUESTION_PAY)
    
    def click_how_many_question(self):
        """Click on 'How many tickets can I book?' question"""
        self.click_question(self.QUESTION_HOW_MANY)
    
    def is_answer_section_visible(self, answer_locator):
        """Check if an answer section is visible in viewport"""
        try:
            element = self.driver.find_element(*answer_locator)
            # Check if element is in viewport
            return self.driver.execute_script(
                "var elem = arguments[0];"
                "var rect = elem.getBoundingClientRect();"
                "return (rect.top >= 0 && rect.bottom <= window.innerHeight);",
                element
            )
        except:
            return False
    
    def is_answer_section_displayed(self, answer_locator):
        """Check if an answer section exists and is displayed"""
        try:
            element = self.driver.find_element(*answer_locator)
            return element.is_displayed()
        except:
            return False
    
    def is_answer_displayed_by_number(self, answer_number):
        """Check if an answer section is displayed by its number (1-8)"""
        if answer_number not in self.ANSWER_LOCATORS:
            raise ValueError(f"Invalid answer number: {answer_number}. Must be 1-8.")
        return self.is_answer_section_displayed(self.ANSWER_LOCATORS[answer_number])
    
    def is_book_ticket_answer_visible(self):
        """Check if book ticket answer section is visible"""
        return self.is_answer_section_displayed(self.ANSWER_BOOK_TICKET)
    
    def is_expired_answer_visible(self):
        """Check if expired answer section is visible"""
        return self.is_answer_section_displayed(self.ANSWER_EXPIRED)
    
    def click_create_account_link(self):
        """Click on 'create an account' link in FAQ answers"""
        link = self.driver.find_element(*self.CREATE_ACCOUNT_LINK)
        self.driver.execute_script('arguments[0].scrollIntoView();', link)
        link.click()
    
    def click_book_ticket_page_link(self):
        """Click on 'Book Ticket page' link in FAQ answers"""
        link = self.driver.find_element(*self.BOOK_TICKET_PAGE_LINK)
        self.driver.execute_script('arguments[0].scrollIntoView();', link)
        link.click()
    
    def get_all_text_content(self):
        """Get all text content from FAQ page for spell checking"""
        return self.driver.find_element(By.TAG_NAME, "body").text
    
    def get_all_questions(self):
        """Get all question texts"""
        questions = self.driver.find_elements(By.CSS_SELECTOR, "ol li a")
        return [q.text for q in questions]
    
    def check_no_misspelled_words(self):
        """Basic check for common misspellings in FAQ page"""
        content = self.get_all_text_content().lower()
        # Check for common words that should be present
        expected_words = ['book', 'ticket', 'expired', 'pay', 'register', 'login']
        found_words = [word for word in expected_words if word in content]
        return len(found_words) == len(expected_words)