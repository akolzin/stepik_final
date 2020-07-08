from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_empty_message(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE)

        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE)
