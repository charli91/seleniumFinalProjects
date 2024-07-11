from pages.auth_login_page import AuthLoginPage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePageLocators:
    sign_in_button = (By.LINK_TEXT, "Sign in")
    product = (By.XPATH, "//a[starts-with(@data-test, 'product')]")


class HomePage(BasePage):
    def click_sign_in(self):
        # clicks 'sign in' link and returns AuthLoginPage instance
        self.driver.find_element(*HomePageLocators.sign_in_button).click()
        return AuthLoginPage(self.driver)

    def click_any_product(self):
        # clicks on fist product displayed
        self.driver.find_element(*HomePageLocators.product).click()
