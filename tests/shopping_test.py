from tests.base_test import BaseTest
from time import sleep


class ShoppingTest(BaseTest):
    # Scenariusz 2: Zakup produktu
    def setUp(self):
        # odnośnik do metody z klasy parent
        super().setUp()
        #     WARUNKI WSTĘPNE
        #   1. Użytkownik niezalogowany
        #   2. Użytkownik znajduje się na stronie dowolnego produktu
        self.go_to_product_page = self.home_page.click_any_product()

    def test_adding_product_to_cart(self):
        """
        TC 001:
        """
        # KROKI:
        #       1.najpierw sprawdzić sobie, że koszyk ikonka się nie wyświetla w ogóle
        #       potem dodać jeden produkt, sprawdzić pierwszy raz że pojawiła się ikona koszyka z numerem 1
        #       potem dodać drugi raz klik i sprawdzić, że zmieniłą sie ikonka na 2

        pass
