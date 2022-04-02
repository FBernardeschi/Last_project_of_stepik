from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.ID, "login_link")
    FORM_LOGIN = (By.NAME, "login_submit")
    FORM_REG = (By.NAME, "registration_submit")