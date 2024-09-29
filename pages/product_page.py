from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPageLocators:
    add_to_cart_button = (By.ID, "btn-add-to-cart")
    # ikona koszyk:
    cart_icon = (By.XPATH, "//a[@data-test='nav-cart']")
    # ikona z numerem:
    cart_number_icon = (By.XPATH, "//a[@data-test='nav-cart']//span[@data-test='cart-quantity']")
    # cart_number_of_elements_added =


class ProductPage(BasePage):
    # kliknięcie ikony koszyka
    def click_add_to_cart(self):
        self.driver.find_element(*ProductPageLocators.add_to_cart_button).click()
