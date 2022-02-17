import time
import pytest

from pages.product_page import ProductPage
from pages.base_page import BasePage

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
parameters = [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9]
# parameter_fail = [7]


# @pytest.mark.parametrize('parameter', [parameters,
#                                        pytest.param(parameter_fail, marks=pytest.mark.xfail)])
@pytest.mark.parametrize('parameter', parameters)
def test_guest_can_add_product_to_basket(browser, parameter):
    page = ProductPage(browser, f"{link}{parameter}")
    page.open()
    page.should_be_button_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_product_add_to_basket()
    page.should_be_message_with_price_basket()
