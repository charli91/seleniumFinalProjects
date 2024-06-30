from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CustomerRegistrationPageLocators:
    first_name_field = (By.XPATH, "//input[@data-test='first-name']")


class CustomerRegistrationPage(BasePage):
    # znalezienie pola input z imieniem
    def input_first_name_field(self, first_name):
        el = self.driver.find_element(*CustomerRegistrationPageLocators.first_name_field)
        el.send_keys(first_name)
