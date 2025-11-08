from pages.base_page import BasePage
from Locators.profile_locators import ProfileLocators

class ProfilePage(BasePage):

    def open_profile(self):
        self.click(ProfileLocators.button_complete_profile_xpath)
        self.click(ProfileLocators.resume_headline_xpath)

    def update_resume_headline(self, text):
        self.click(ProfileLocators.edit_icon_resume_headline)
        self.type(ProfileLocators.input_field_xpath, text)
        self.click(ProfileLocators.save_button_xpath)
