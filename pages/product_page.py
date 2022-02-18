from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_button_add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_add_to_basket.click()
        assert button_add_to_basket, "Button 'Add to basket' is not presented"

    def should_be_message_product_add_to_basket(self):
        message_product_add_to_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_ADD_TO_BASKET)
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        assert name_book.text == message_product_add_to_basket.text, "Incorrect product in basket"

    def should_be_message_with_price_basket(self):
        message_with_price_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRICE_BASKET)
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        assert price_book.text == message_with_price_basket.text, "Incorrect price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def element_should_be_disappeared(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADD_TO_BASKET), \
            "Success message not disappeared"
