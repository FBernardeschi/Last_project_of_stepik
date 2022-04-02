from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login link is not presented"
        self.browser.find_element(*LoginPageLocators.LOGIN_URL).click()
        assert "login" in self.browser.current_url, "There is not login in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Form login is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REG), "Form Registration is not present"