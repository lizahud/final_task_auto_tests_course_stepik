import time
import pytest
import faker

from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
# from pages.login_page import LoginPage, email, password

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
parameters = [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9]
# parameters = [0]
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"


@pytest.mark.new_class
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        time.sleep(10)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    # Открываем страницу товара
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    # @pytest.mark.parametrize('parameter', parameters)
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        # page.should_not_be_success_message()
        page.should_be_button_add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_message_product_add_to_basket()
        page.should_be_message_with_price_basket()
        # page.element_should_be_disappeared()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
# Открываем страницу товара
# Добавляем товар в корзину
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.element_should_be_disappeared()
# Открываем страницу товара
# Добавляем товар в корзину
# Проверяем, что нет сообщения об успехе с помощью is_disappeared


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_button_go_to_basket()
    time.sleep(5)
    page.in_basket_no_product()
    page.should_be_text_about_empty_basket()
# Гость открывает страницу товара
# Переходит в корзину по кнопке в шапке
# Ожидаем, что в корзине нет товаров
# Ожидаем, что есть текст о том что корзина пуста


@pytest.mark.parametrize('parameter', parameters)
def test_guest_can_add_product_to_basket(browser, parameter):
    page = ProductPage(browser, f"{link}{parameter}")
    page.open()
    # page.should_not_be_success_message()
    page.should_be_button_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_product_add_to_basket()
    page.should_be_message_with_price_basket()
    # page.element_should_be_disappeared()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
# Открываем страницу товара
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present


@pytest.mark.new
def test_registration(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.register_new_user(email, password)
    time.sleep(10)
    page.should_be_authorized_user()