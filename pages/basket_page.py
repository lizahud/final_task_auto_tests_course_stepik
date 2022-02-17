from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def in_basket_no_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BUTTON_CHECKOUT), "Basket not empty"

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), "No message about empty basket"
