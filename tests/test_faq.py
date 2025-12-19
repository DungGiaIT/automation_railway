from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from base_test import BaseTest
import time


class TestFAQ(BaseTest):
    
    def test_FAQ_001(self):
        self.home_page.go_to_faq_page()
        
        # Verify FAQ page is displayed
        self.assertIn("/Page/FAQ.cshtml", self.driver.current_url)
        
        # Verify FAQ header is displayed
        header = self.faq_page.get_page_header()
        self.assertEqual(
            header,
            "Frequently Asked Questions",
            "FAQ header is not displayed correctly"
        )
        
        # Verify navigation bar is visible
        self.assertTrue(
            self.faq_page.is_navigation_bar_visible(),
            "Navigation bar is not visible"
        )
        
        # Verify footer is visible
        self.assertTrue(
            self.faq_page.is_footer_visible(),
            "Footer is not visible"
        )
        
        # Check for basic content integrity (no major misspellings)
        self.assertTrue(
            self.faq_page.check_no_misspelled_words(),
            "Some expected words are missing from FAQ page"
        )
        
        # Verify questions are displayed
        questions = self.faq_page.get_all_questions()
        self.assertGreater(
            len(questions),
            0,
            "No questions found on FAQ page"
        )
        
        print(f"Found {len(questions)} questions on FAQ page")
    
    def test_FAQ_002(self):
        self.home_page.go_to_faq_page()
        
        # Test all 8 questions
        question_names = [
            "How to book a ticket?",
            "Why do my tickets get expired?",
            "How to pay for my tickets?",
            "How many tickets can I book?",
            "Filter in My Ticket page",
            "Change station/date",
            "Browser support",
            "Other questions"
        ]
        
        for question_num in range(1, 9):
            # Scroll back to top before clicking each question
            self.driver.execute_script("window.scrollTo(0, 0);")
            
            # Click the question
            self.faq_page.click_question_by_number(question_num)
            time.sleep(0.5)
            
            # Verify the corresponding answer section is displayed
            self.assertTrue(
                self.faq_page.is_answer_displayed_by_number(question_num),
                f"Answer section {question_num} ({question_names[question_num-1]}) is not visible after clicking question"
            )
            
            print(f"Question {question_num} ({question_names[question_num-1]}) - Answer displayed: OK")
    
    def test_FAQ_003(self):
        self.home_page.go_to_faq_page()

        
        # Test 1: Check "create an account" link
        # Click on "How to book a ticket?" question (question #1)
        self.faq_page.click_book_ticket_question(1)
        
        # Click on "create an account" link in the answer
        self.faq_page.click_create_account_link()
        time.sleep(0.5)
        
        # Verify navigation to register page
        self.assertIn(
            "/Account/Register.cshtml",
            self.driver.current_url,
            "Did not navigate to register page after clicking 'create an account' link"
        )
        print("'Create an account' link works correctly")
        
        # Go back to FAQ page
        self.home_page.go_to_faq_page()
        
        # Test 2: Check "book ticket page" link
        # Click on "How to book a ticket?" question (question #1)
        self.faq_page.click_book_ticket_question(1)

        
        # Click on "Book Ticket page" link in the answer
        self.faq_page.click_book_ticket_page_link()
        time.sleep(0.5)
        
        # Verify navigation to book ticket page
        current_url = self.driver.current_url
        self.assertTrue(
            "/Page/BookTicketPage" in current_url or "/BookTicketPage.cshtml" in current_url,
            f"Did not navigate to book ticket page. Current URL: {current_url}"
        )
        print("'Book Ticket page' link works correctly")