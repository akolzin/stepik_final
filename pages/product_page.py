from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):

    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.CLICK_BUTTON), "Button is not presented"
        button = self.browser.find_element(*ProductPageLocators.CLICK_BUTTON)
        button.click()

    def find_product_name(self):
        product_name_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name_in_basket == product_name_on_page, "Name is not same"

    def find_product_price(self):
        product_price_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price_in_basket == product_price_on_page, "Name is not same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is dissapeared, but should not be"