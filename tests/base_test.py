import unittest
from selenium import webdriver

from pages.auth_login_page import AuthLoginPage
from pages.home_page import HomePage
from pages.customer_registration_page import CustomerRegistrationPage

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # wejście na bazową stronę internetową
        self.driver.get("https://practicesoftwaretesting.com/#/")
        # Dodaje bezwarunkowe czekanie na elementy
        self.driver.implicitly_wait(5)
        self.home_page = HomePage(self.driver)
        self.auth_login_page = AuthLoginPage(self.driver)
        self.customer_registration_page = CustomerRegistrationPage(self.driver)

    def tearDown(self):
        self.driver.quit()