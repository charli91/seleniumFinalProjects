from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPageLocators:
    add_to_cart_button = (By.XPATH, "//button[@id='btn-add-to-cart']")
    # ikona koszyk:
    cart_icon = (By.XPATH, "//a[@data-test='nav-cart']")
    # ikona z numerem:
    cart_number_icon = (By.XPATH, "//a[@data-test='nav-cart']//span[@data-test='cart-quantity']")
    # cart_number_of_elements_added =
    toast_container = (By.XPATH, "//div[@id='toast-container'][@class='toast-top-right toast-container']/div[1]")


class ProductPage(BasePage):
    # kliknięcie ikony koszyka
    def click_add_to_cart(self):
        self.driver.find_element(ProductPageLocators.add_to_cart_button).click()
    # nie widać kliknięcia. a xpath jest ok
    # do shopping_test dodawanie do koszyka - nie działa to.
    def get_added_to_cart_toast_message(self):
        self.driver.find_element(ProductPageLocators.toast_container).is_displayed()
    #     # self.driver.find_element(ProductPageLocators.toast_container).text
    #     assert self.driver.find_element(ProductPageLocators.toast_container).is_displayed()
