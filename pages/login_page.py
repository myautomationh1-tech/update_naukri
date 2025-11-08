from pages.base_page import BasePage
from Locators.login_locators import LoginLocators

class LoginPage(BasePage):

    def open_naukri(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def click_login(self):
        self.click(LoginLocators.login_button_xpath)

    def login(self, email, password):
        self.type(LoginLocators.email_input_xpath, email)
        self.type(LoginLocators.password_input_xpath, password)
        self.click(LoginLocators.login_submit_btn)
