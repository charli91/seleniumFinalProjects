from pages.auth_login_page import AuthLoginPage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePageLocators:
    sign_in_button = (By.LINK_TEXT, "Sign in")


class HomePage(BasePage):
    def click_sign_in(self):
        # clicks 'sign in' link and returns AuthLoginPage instance
        self.driver.find_element(*HomePageLocators.sign_in_button).click()
        return AuthLoginPage(self.driver)
