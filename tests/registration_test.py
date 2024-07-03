from tests.base_test import BaseTest
from test_data.test_data import RegistrationData
from time import sleep


class RegistrationTest(BaseTest):
    # Scenariusz 1: rejestracja nowego użytkownika
    def setUp(self):
        # odnośnik do metody z klasy parent
        super().setUp()
        self.test_data = RegistrationData()

    def test_no_phone_number_entered(self):
        """
        TC 001: Brak podania numeru telefonu w formularzu rejestracji
        """
        # KROKI:
        #     1. Kliknij ‘Sign in’
        self.auth_login_page = self.home_page.click_sign_in()
        #     2. Kliknij ‘Register your account’
        self.register = self.auth_login_page.click_register_btn()
        #     3. Wprowadź Pierwszę imię
        self.register_first_name = self.customer_registration_page.input_first_name(self.test_data.first_name)
        #     4. Wprowadź nazwisko
        self.register_last_name = self.customer_registration_page.input_last_name(self.test_data.last_name)
        #     5. Wprowadź datę urodzenia
        self.register_date_of_birth = self.customer_registration_page.input_date_of_birth(self.test_data.date_of_birth)
        #     6. Wprowadź adres
        self.register_address = self.customer_registration_page.input_address(self.test_data.address)
        #     7. Wprowadź kod pocztowy
        self.register_postcode = self.customer_registration_page.input_postal_code(self.test_data.postal_code)
        #     8. Wprowadź Miasto
        self.register_city = self.customer_registration_page.input_city(self.test_data.city)
        #     9. Wprowadź województwo (stan)
        self.register_state = self.customer_registration_page.input_state(self.test_data.state)
        #     10. Wybierz z listy rozwijanej kraj
        self.register_country = self.customer_registration_page.select_country(self.test_data.country)
        #     11. Wprowadź adres email
        self.register_email = self.customer_registration_page.input_email(self.test_data.email)
        #     12. Wprowadź hasło min. 6 znaków
        self.register_passwd = self.customer_registration_page.input_passwd(self.test_data.passwd)
        #     13. Kliknij ‘Register’
        self.accept_registration = self.customer_registration_page.click_register()

        # OCZEKIWANE REZULTATY:
        #       1. użytkownik otrzymuje informację, że popełnił błąd
        #       w postaci pojawienia się czerwonego okienka pod polem z błędem
        # sprawdzenie, czy istnieje walidacja
        self.phone_number_validation = self.customer_registration_page.get_phone_number_validation_message()

        #       2. Użytkownik otrzymuje informację, że numer telefonu jest wymagany
        # porównanie otrzymanego komunikatu
        self.assertEqual('Phone is required.', self.customer_registration_page.get_error_messages()[0])

        #       3. Na ekranie wyświetla się tylko jedna wiadomość walidacyjna

