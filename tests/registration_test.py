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
        # TC 001: Brak podania numeru telefonu w formularzu rejestracji
        # KROKI:
        #     1. Kliknij ‘Sign in’
        self.auth_login_page = self.home_page.click_sign_in()
        #     2. Kliknij ‘Register your account’
        self.register_name = self.customer_registration_page.input_first_name_field(self.test_data.first_name)
        #     3. Wprowadź Pierwszę imię
        #     4. Wprowadź nazwisko
        #     5. Wprowadź datę urodzenia
        #     6. Wprowadź adres
        #     7. Wprowadź kod pocztowy
        #     8. Wprowadź Miasto
        #     9. Wprowadź województwo (stan)
        #     10. Wybierz z listy rozwijanej kraj
        #     11. Wprowadź adres email
        #     12. Wprowadź hasło min. 6 znaków
        #     13. Kliknij ‘Register’
