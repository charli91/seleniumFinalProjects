from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AuthLoginPageLocators:
    register_button = (By.LINK_TEXT, "Register your account")


class AuthLoginPage(BasePage):
    def click_register_btn(self):
        self.driver.find_element(*AuthLoginPageLocators.register_button).click()