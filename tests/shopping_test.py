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
        #   3. Użytkownik nie posiada żadnych produktów w koszyku

    def test_adding_product_to_cart(self):
        """
        TC 001: Dodanie pierwszego produktu do koszyka
        """
        # KROKI:
        #   1. Kliknij przycisk 'Add to cart'
        self.click_add_to_cart = self.product_page.click_add_to_cart


        # OCZEKIWANE REZULTATY:
        #       1. Użytkownik otrzymuje informację o dodaniu produktu do koszyka poprzez
        #       wyświetlenie toast message
        # sleep(3)
        # self.assertEqual(self.product_page.get_added_to_cart_toast_message(), '1')
        # sleep(3)
        #       2. Po dodaniu pierwszego produktu pojawia się ikonka z jedynką
        pass
