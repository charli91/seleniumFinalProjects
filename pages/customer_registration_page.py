from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CustomerRegistrationPageLocators:
    first_name_field = (By.XPATH, "//input[@data-test='first-name']")
    last_name_field = (By.ID, "last_name")
    # data urodzenie
    # adres
    # kod pocztowy
    # Miasto
    # województwo (stan)
    # wybierz z listy- kraj
    choose_country_field = (By.XPATH, "//select[@data-test='country']")
    # wprowadź adres email
    # wprowadź hasło min. 6 znaków
    # button register


class CustomerRegistrationPage(BasePage):
    # znalezienie pola input z imieniem
    def input_first_name_field(self, first_name):
        el = self.driver.find_element(*CustomerRegistrationPageLocators.first_name_field)
        el.send_keys(first_name)

    def input_last_name_field(self, last_name):
        self.driver.find_element(*CustomerRegistrationPageLocators.last_name_field).send_keys(last_name)

    def select_country(self, country):
        country_select = Select(self.driver.find_element(*CustomerRegistrationPageLocators.choose_country_field))
        country_select.select_by_value(country)