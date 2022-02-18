import faker
import time

from .base_page import BasePage
from .locators import LoginPageLocators

f = faker.Faker()
# email = f.email()
# email = str(time.time()) + "@fakemail.org"
# password = "fPY-3S7-GAW-hEd"
# password = "fPY"


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        # assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        current_url = self.browser.current_url
        assert "login" in current_url, f"Incorrect url {current_url}, must be with 'login in link'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = "fPY-3S7-GAW-hEd"
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_input.send_keys(password)
        password_confirm_input = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
        password_confirm_input.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        register_button.click()

