from tests.base_test import BaseTest
from test_data.test_data_manual import RegistrationDataManual
from test_data.test_data_faker import RegistrationDataFaker
import test_data.test_data_manual
from time import sleep
from ddt import ddt, data, unpack


@ddt
class RegistrationTest(BaseTest):
    # Scenariusz 1: rejestracja nowego użytkownika
    def setUp(self):
        # odnośnik do metody z klasy parent
        super().setUp()
        self.data_manual = RegistrationDataManual()
        self.data_faker = RegistrationDataFaker()
        #     WARUNKI WSTĘPNE
        #     1. Kliknij ‘Sign in’
        self.auth_login_page = self.home_page.click_sign_in()
        #     2. Kliknij ‘Register your account’
        self.register = self.auth_login_page.click_register_btn()

    def test_no_phone_number_entered(self):
        """
        TC 001: Brak podania numeru telefonu w formularzu rejestracji
        """
        # KROKI:
        #     1. Wprowadź imię
        self.register_first_name = self.customer_registration_page.input_first_name(self.data_manual.first_name)
        #     2. Wprowadź nazwisko
        self.register_last_name = self.customer_registration_page.input_last_name(self.data_manual.last_name)
        #     3. Wprowadź datę urodzenia
        self.register_date_of_birth = self.customer_registration_page.input_date_of_birth(
            self.data_manual.date_of_birth)
        #     4. Wprowadź adres
        self.register_address = self.customer_registration_page.input_address(self.data_manual.address)
        #     5. Wprowadź kod pocztowy
        self.register_postcode = self.customer_registration_page.input_postal_code(self.data_manual.postal_code)
        #     6. Wprowadź Miasto
        self.register_city = self.customer_registration_page.input_city(self.data_manual.city)
        #     7. Wprowadź województwo (stan)
        self.register_state = self.customer_registration_page.input_state(self.data_manual.state)
        #     8. Wybierz z listy rozwijanej kraj
        self.register_country = self.customer_registration_page.select_country(self.data_manual.country)
        #     9. Wprowadź adres email
        self.register_email = self.customer_registration_page.input_email(self.data_manual.email)
        #     10. Wprowadź hasło min. 6 znaków
        self.register_passwd = self.customer_registration_page.input_passwd(self.data_manual.passwd)
        # # testowo- jakby był dodany nr tel.- czyli jakby walidacja się nie pojawiła
        # self.register_phone_number = self.customer_registration_page.input_phone_number(self.test_data.phone_number)
        #    11. Kliknij ‘Register’
        self.accept_registration = self.customer_registration_page.click_register()

        # OCZEKIWANE REZULTATY:
        #       1. użytkownik otrzymuje informację, że popełnił błąd
        #       w postaci pojawienia się czerwonego okienka pod polem z błędem
        # sprawdzenie, czy istnieje walidacja;
        # to niżej powoduje, że test przechodzi na pass nawet, jak nie ma tej walidacji.
        # while True:
        #     try:
        #         self.phone_number_validation = self.customer_registration_page.get_phone_number_validation_message()
        #         break
        #     except Exception:
        #         break
        self.phone_number_validation = self.customer_registration_page.get_phone_number_validation_message()

        #       2. Użytkownik otrzymuje informację, że numer telefonu jest wymagany
        # porównanie otrzymanego komunikatu
        self.assertEqual('Phone is required.', self.customer_registration_page.get_error_messages()[0])

        #       3. Na ekranie wyświetla się tylko jedna wiadomość walidacyjna
        self.assertEqual(1, len(self.customer_registration_page.get_error_messages()))

    def test_no_last_name_entered(self):
        """
        TC 002: Brak podania nazwiska w formularzu rejestracji
        """

        # KROKI:
        #     1. Wprowadź imię
        self.register_first_name = self.customer_registration_page.input_first_name(self.data_faker.first_name)
        #     2. Wprowadź datę urodzenia
        self.register_date_of_birth = self.customer_registration_page.input_date_of_birth(self.data_faker.date_of_birth)
        #     3. Wprowadź adres
        self.register_address = self.customer_registration_page.input_address(self.data_faker.address)
        #     4. Wprowadź kod pocztowy
        self.register_postcode = self.customer_registration_page.input_postal_code(self.data_faker.postal_code)
        #     5. Wprowadź Miasto
        self.register_city = self.customer_registration_page.input_city(self.data_faker.city)
        #     6. Wprowadź województwo (stan)
        self.register_state = self.customer_registration_page.input_state(self.data_faker.state)
        #     7. Wybierz z listy rozwijanej kraj
        self.register_country = self.customer_registration_page.select_country(self.data_faker.country)
        #     8. Wprowadź numer telefonu
        self.register_phone_number = self.customer_registration_page.input_phone_number(self.data_faker.phone_number)
        #     9. Wprowadź adres email
        self.register_email = self.customer_registration_page.input_email(self.data_faker.email)
        #     10. Wprowadź hasło min. 6 znaków
        self.register_passwd = self.customer_registration_page.input_passwd(self.data_faker.passwd)
        #    11. Kliknij ‘Register’
        self.accept_registration = self.customer_registration_page.click_register()
        # sleep(5)
        """
        TODO: ASSERTIONS IN 2ND TC
        """

    @data(*test_data.test_data_manual.get_csv_data())
    def test_not_strong_enough_password(self):
        """
                TC 001:
                """
        # KROKI:
        #       1.
        pass
