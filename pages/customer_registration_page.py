from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CustomerRegistrationPageLocators:
    first_name_field = (By.XPATH, "//input[@data-test='first-name']")
    last_name_field = (By.ID, "last_name")
    # data urodzenie
    date_of_birth_field = (By.XPATH, "//input[@data-test='dob']")
    # adres
    address_field = (By.XPATH, "//input[@data-test='address']")
    # kod pocztowy
    postal_code_field = (By.XPATH, "//input[@data-test='postcode']")
    # Miasto
    city_field = (By.XPATH, "//input[@data-test='city']")
    # województwo (stan)
    state_field = (By.XPATH, "//input[@data-test='state']")
    # wybierz z listy- kraj
    chosen_country_field = (By.XPATH, "//select[@data-test='country']")
    # wprowadź adres email
    email_field = (By.XPATH, "//input[@data-test='email']")
    # wprowadź hasło min. 6 znaków
    passwd_field = (By.XPATH, "//input[@data-test='password']")
    # button register
    accept_registration_button = (By.XPATH, "//button[@data-test='register-submit']")


class CustomerRegistrationPage(BasePage):
    # znalezienie pola input z imieniem
    def input_first_name(self, first_name):
        el = self.driver.find_element(*CustomerRegistrationPageLocators.first_name_field)
        el.send_keys(first_name)

    def input_last_name(self, last_name):
        self.driver.find_element(*CustomerRegistrationPageLocators.last_name_field).send_keys(last_name)

    def select_country(self, country):
        country_select = Select(self.driver.find_element(*CustomerRegistrationPageLocators.chosen_country_field))
        country_select.select_by_value(country)

    def input_date_of_birth(self, date_of_birth):
        self.driver.find_element(*CustomerRegistrationPageLocators.date_of_birth_field).send_keys(date_of_birth)

    def input_address(self, address):
        self.driver.find_element(*CustomerRegistrationPageLocators.address_field).send_keys(address)

    def input_postal_code(self, postcode):
        self.driver.find_element(*CustomerRegistrationPageLocators.postal_code_field).send_keys(postcode)

    def input_city(self, city):
        self.driver.find_element(*CustomerRegistrationPageLocators.city_field).send_keys(city)

    def input_state(self, state):
        self.driver.find_element(*CustomerRegistrationPageLocators.state_field).send_keys(state)

    def input_email(self, email):
        self.driver.find_element(*CustomerRegistrationPageLocators.email_field).send_keys(email)

    def input_passwd(self, passwd):
        self.driver.find_element(*CustomerRegistrationPageLocators.passwd_field).send_keys(passwd)

    def click_register(self):
        self.driver.find_element(*CustomerRegistrationPageLocators.accept_registration_button).click()

    # sprawdza liczbę wyświetlonych okienek walidacyjnych

    # zwraca wiadomości wysłane do użytkownika w okienkach walidacyjnych w postaci listy